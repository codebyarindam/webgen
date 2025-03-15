const OLLAMA_API_URL = "http://61.2.142.91:4434/api/chat"; // Ollama API URL
const cors = require("cors");
const mysql = require("mysql");
const { execFile, exec } = require("child_process");
const path = require("path");
const fs = require("fs");
const axios = require("axios"); // Added axios import
const express = require("express");
const app = express();

const { spawn } = require("child_process");

// Enable CORS
app.use(cors());
app.use(express.json());

const GENERATED_FILES_DIR = path.join(__dirname, "generated_files");

// Ensure directory exists
// const fs = require("fs");
if (!fs.existsSync(GENERATED_FILES_DIR)) {
  fs.mkdirSync(GENERATED_FILES_DIR);
}

// Database configuration
const dbConfig = {
  host: "88.150.227.117",
  user: "nrktrn_web",
  password: "nrktrn11",
  database: "nrkindex_trn",
};
const sbConfig = {
  host: "88.150.227.117",
  user: "nrktrn_web_admin",
  password: "R7$Fp3465%^%",
  port: "3306",
  database: "nrkindex_trn",
};
// MySQL connection
const dbConnection = mysql.createConnection(dbConfig);

const sbConnection = mysql.createConnection(sbConfig);

sbConnection.connect((err) => {
  if (err) {
    console.error("Error connecting to the database:", err);
    process.exit(1);
  }
  console.log("Database connected!");
});
// Directory for generated files
const GENERATED_CODE_DIR = path.join(__dirname, "generated_code");
if (!fs.existsSync(GENERATED_CODE_DIR)) {
  fs.mkdirSync(GENERATED_CODE_DIR);
  console.log(`Created directory for generated code: ${GENERATED_CODE_DIR}`);
}

// Directory for uploaded files
const UPLOAD_FOLDER = path.join(__dirname, "uploads");
if (!fs.existsSync(UPLOAD_FOLDER)) {
  fs.mkdirSync(UPLOAD_FOLDER);
  console.log(`Created directory for uploaded files: ${UPLOAD_FOLDER}`);
}

// Chat API for interaction with Ollama API
app.post("/chat", async (req, res) => {
  try {
    const { userInput } = req.body;
    if (!userInput) {
      return res.status(400).json({ error: "User input is required" });
    }

    console.log("Sending request to Ollama API...");
    const ollamaResponse = await axios.post(
      OLLAMA_API_URL,
      {
        model: "llama3.2",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: userInput },
        ],
        stream: false,
      },
      { headers: { "Content-Type": "application/json" } }
    );

    console.log("Received response from Ollama API");
    res.json({ response: ollamaResponse.data.content });
  } catch (error) {
    console.error("Error communicating with Ollama API:", error);
    res.status(500).json({ error: "Failed to get response from Ollama API" });
  }
});

const logger = require("./logger"); // Import the logger

app.use((req, res, next) => {
  logger.info(`Received request: ${req.method} ${req.url}`);
  next();
});

// Example logging in API routes
app.post("/api/generate-insert", async (req, res) => {
  const { prompt } = req.body;
  if (!prompt) {
    logger.warn("Missing prompt in request");
    return res.status(400).json({ error: "Prompt is required" });
  }

  try {
    logger.info("Calling external API for SQL generation");
    const response = await axios.post(OLLAMA_API_URL, {
      model: "llama3.2",
      messages: [{ role: "user", content: prompt }],
    });

    logger.info("SQL Generation successful");
    res.json({ sql: response.data.content });
  } catch (error) {
    logger.error(`Error generating SQL: ${error.message}`);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.get("/api/logs", (req, res) => {
  const logFilePath = path.join(__dirname, "logs/app.log");

  if (!fs.existsSync(logFilePath)) {
    return res.status(404).json({ error: "Log file not found" });
  }

  fs.readFile(logFilePath, "utf8", (err, data) => {
    if (err) {
      logger.error(`Error reading log file: ${err.message}`);
      return res.status(500).json({ error: "Error reading log file" });
    }

    const logEntries = data.split("\n").filter((line) => line.trim() !== "");
    res.json(logEntries);
  });
});

// Global error handler
app.use((err, req, res, next) => {
  logger.error(`Unhandled error: ${err.message}`);
  res.status(500).json({ error: "Internal Server Error" });
});

// Serve generated code as raw text
app.get("/generated-code/:filename", (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(GENERATED_CODE_DIR, filename);

  console.log(`Fetching generated code file: ${filename}`);
  if (fs.existsSync(filePath)) {
    fs.readFile(filePath, "utf8", (err, data) => {
      if (err) {
        return res.status(500).json({ error: "Error reading the file." });
      }
      res.setHeader("Content-Type", "text/plain");
      res.send(data);
    });
  } else {
    res.status(404).json({ error: "File not found." });
  }
});

// Check Python code for errors and execute it
function checkPythonCode(filename, callback) {
  console.log(`Checking Python code for errors in file: ${filename}`);
  execFile("python", ["-m", "py_compile", filename], (err, stdout, stderr) => {
    if (err) {
      console.error(`Error compiling Python file: ${stderr}`);
      return callback({ status: "error", error: stderr });
    }

    console.log("Python code compiled successfully. Executing...");
    execFile("python", [filename], (execErr, execStdout, execStderr) => {
      if (execErr) {
        console.error(`Error executing Python file: ${execStderr}`);
        return callback({ status: "error", error: execStderr });
      }
      console.log("Python code executed successfully");
      callback({ status: "success", output: execStdout });
    });
  });
}

// Get parameters for a given disease
function getParametersForDisease(diseaseName, callback) {
  console.log(`Fetching parameters for disease: ${diseaseName}`);
  const query = `
    SELECT PARENT_ID FROM ai_master
    WHERE PARENT_ID IS NOT NULL AND AI_TYPE='PIndex' AND AI_PROGRAM=?
  `;
  dbConnection.query(query, [diseaseName], (err, result) => {
    if (err) {
      console.error("Database error:", err);
      return callback([]);
    }
    if (result.length === 0) {
      console.log(`No parameters found for disease: ${diseaseName}`);
      return callback([]);
    }

    const parentId = result[0].PARENT_ID;
    const paramQuery = "SELECT name FROM procedure_type WHERE parent = ?";
    dbConnection.query(paramQuery, [parentId], (err, params) => {
      if (err) {
        console.error("Database error fetching parameters:", err);
        return callback([]);
      }
      console.log(`Fetched parameters for disease: ${diseaseName}`);
      callback(params.map((param) => param.name));
    });
  });
}

// Generate synthetic data
function generateSyntheticData(disease, params, numSamples = 100) {
  console.log(
    `Generating synthetic data for disease: ${disease} with ${numSamples} samples`
  );
  const data = {};
  params.forEach((param) => {
    data[param] = Array.from({ length: numSamples }, () => Math.random() * 100);
  });
  data[`${disease} Outcome`] = Array.from({ length: numSamples }, () =>
    Math.random() < 0.5 ? 0 : 1
  );

  const timestamp = new Date().toISOString().replace(/[-T:.Z]/g, "");
  const filename = path.join(
    GENERATED_CODE_DIR,
    `${disease.toLowerCase()}_data_${timestamp}.csv`
  );
  const csvContent = Object.keys(data)
    .map((key) => `${key},${data[key].join(",")}`)
    .join("\n");

  fs.writeFileSync(filename, csvContent);
  console.log(`Synthetic data for disease ${disease} saved to ${filename}`);
  return filename;
}

// Generate ML code
function generateMLCode(disease, params, datasetFilename, callback) {
  console.log(`Generating ML code for disease: ${disease}`);
  const timestamp = new Date().toISOString().replace(/[-T:.Z]/g, "");
  const filename = path.join(
    GENERATED_CODE_DIR,
    `Train${disease.replace(/ /g, "")}Model_${timestamp}.py`
  );

  const mlCode = `import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# Load dataset
df = pd.read_csv('${datasetFilename}')

X = df[${JSON.stringify(params)}]
y = df['${disease} Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"AUC: {auc}")
`;

  fs.writeFileSync(filename, mlCode);
  console.log(`ML code generated and saved to ${filename}`);
  callback(filename);
}

app.post("/generate", (req, res) => {
  const { disease, num_samples = 100 } = req.body;

  console.log(
    `Request to generate synthetic data and ML code for disease: ${disease}`
  );
  getParametersForDisease(disease, (params) => {
    if (!params || params.length === 0) {
      console.log(`No parameters found for disease: ${disease}`);
      return res
        .status(404)
        .json({ error: `Disease '${disease}' not found or has no parameters` });
    }

    const datasetFilename = generateSyntheticData(disease, params, num_samples);
    generateMLCode(disease, params, datasetFilename, (mlCodeFilename) => {
      fs.readFile(mlCodeFilename, "utf8", (err, codeContent) => {
        if (err) {
          console.error("Error reading the ML code file:", err);
          return res
            .status(500)
            .json({ error: "Error reading the ML code file." });
        }

        console.log("Sending generated dataset and code content");
        res.json({
          dataset: path.basename(datasetFilename),
          code: path.basename(mlCodeFilename),
          codeContent,
        });
      });
    });
  });
});

// API to execute Python code
app.post("/execute", (req, res) => {
  const { filename } = req.body;

  console.log(`Request to execute Python code file: ${filename}`);
  if (!filename) {
    return res
      .status(400)
      .json({ status: "error", error: "Filename is required." });
  }

  const filePath = path.join(UPLOAD_FOLDER, filename);

  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ status: "error", error: "File not found." });
  }

  exec(`python "${filePath}"`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python file: ${stderr || error.message}`);
      return res
        .status(500)
        .json({ status: "error", error: stderr || error.message });
    }

    console.log("Python code executed successfully");
    res.status(200).json({ status: "success", output: stdout });
  });
});

// API to download files
app.get("/download/:filename", (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(GENERATED_CODE_DIR, filename);

  console.log(`Request to download file: ${filename}`);
  if (fs.existsSync(filePath)) {
    res.download(filePath, filename, (err) => {
      if (err) {
        console.error("Error occurred during file download:", err);
        return res
          .status(500)
          .json({ error: "Error occurred during file download." });
      }
    });
  } else {
    res.status(404).json({ error: "File not found" });
  }
});

// Save file path to the database
function saveFilePathToDb(userId, filePath) {
  console.log(`Saving file path to database for user ID: ${userId}`);
  const connection = mysql.createConnection(dbConfig);

  connection.connect((err) => {
    if (err) {
      console.error(`Database connection error: ${err.message}`);
      return;
    }

    const query = `
      INSERT INTO USER_PYTHON_SAVE (USERID, PYTHON_PATH, INSRT_DTM)
      VALUES (?, ?, NOW())
    `;

    connection.query(query, [userId, filePath], (err) => {
      if (err) {
        console.error(`Error saving file path to database: ${err.message}`);
      }
    });

    connection.end();
  });
}

app.get("/api/aia_project", (req, res) => {
  console.log("Fetching data from AIA_PROJECT");

  sbConnection.query("SELECT * FROM AIA_PROJECT", (err, results) => {
    if (err) {
      console.error("Error fetching data:", err);
      res.status(500).send("Error fetching data");
      return;
    }
    console.log("Fetched Data:", results); // Debugging
    res.json(results);
  });
});

// Fetch data from AIA_MODULE
app.get("/api/aia_module", (req, res) => {
  console.log("Fetching data from AIA_MODULE");

  // Modify the SQL query to only fetch the 'module_name' column (or whatever column represents the module)
  sbConnection.query("SELECT module_name FROM AIA_MODULE", (err, results) => {
    if (err) {
      console.error("Error fetching data:", err);
      res.status(500).send("Error fetching data");
      return;
    }
    res.json(results); // Return only the module names
  });
});

// Update data in AIA_MODULE
// app.put("/api/aia_module/:id", (req, res) => {
//   const { id } = req.params;
//   const { name, description } = req.body; // Replace with your columns

//   console.log(`Updating data in AIA_MODULE for ID: ${id}`);
//   const query = "UPDATE AIA_MODULE SET name = ?, description = ? WHERE id = ?";

//   dbConnection.query(query, [name, description, id], (err, results) => {
//     if (err) {
//       console.error("Error updating data:", err);
//       res.status(500).send("Error updating data");
//       return;
//     }
//     console.log(`Data updated successfully for ID: ${id}`);
//     res.json({ message: "Data updated successfully", results });
//   });
// });

// Fetch all projects
// Fetch project names

app.get("/projects", (req, res) => {
  const sql = "SELECT project_id, project_name FROM AIA_PROJECT";
  sbConnection.query(sql, (err, result) => {
    if (err) {
      console.error("Error fetching projects:", err);
      return res.status(500).json({ error: "Database error" });
    }
    res.json({ success: true, data: result });
  });
});

// app.get("/modules", (req, res) => {
//   const { project_name } = req.query;

//   if (!project_name) {
//     return res.status(400).json({ success: false, message: "Project name is required" });
//   }

//   const sql = `
//     SELECT m.module_name
//     FROM AIA_MODULE m
//     JOIN AIA_PROJECT p ON m.project_id = p.project_id
//     WHERE p.project_name = ?`;

//   sbConnection.query(sql, [project_name], (err, result) => {
//     if (err) {
//       console.error("Error fetching modules:", err);
//       return res.status(500).json({ success: false, message: "Database error" });
//     }
//     res.json({ success: true, data: result });
//   });
// });

app.get("/modules", (req, res) => {
  const { project_name } = req.query;

  if (!project_name) {
    return res
      .status(400)
      .json({ success: false, message: "Project name is required" });
  }

  const sql = `
    SELECT m.module_id, m.module_name 
    FROM AIA_MODULE m 
    JOIN AIA_PROJECT p ON m.project_id = p.project_id 
    WHERE p.project_name = ?`;

  sbConnection.query(sql, [project_name], (err, result) => {
    if (err) {
      console.error("Error fetching modules:", err);
      return res
        .status(500)
        .json({ success: false, message: "Database error" });
    }
    res.json({ success: true, data: result });
  });
});

// Endpoint to handle module generation
async function llamaApiCall(prompt) {
  const OLLAMA_API_URL = "http://61.2.142.91:4434/api/chat";
  const HEADERS = { "Content-Type": "application/json" };

  console.log("Sending request to Ollama API with prompt:", prompt);
  try {
    const response = await axios.post(
      OLLAMA_API_URL,
      {
        model: "llama3.1",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: prompt },
        ],
        stream: false,
      },
      { headers: HEADERS }
    );

    console.log("Ollama API response received:", response.data);
    return response.data.message?.content || "Error: Response not available.";
  } catch (error) {
    console.error("Error generating response:", error);
    return "Error generating response";
  }
}

app.post("/generate-project", async (req, res) => {
  const { description, projectName } = req.body;

  try {
    // Call the Ollama API to generate project code based on the description
    const generatedCode = await llamaApiCall(description);

    // Save the data into the database
    db.query(
      "INSERT INTO AIA_USER_PROMPTS (INITIAL_PROMPT, PROJECT_NAME, PLATFORM, CODING_REQUIRED, CREATED_AT) VALUES (?, ?, ?, ?, NOW())",
      [description, projectName, "Next.js", true],
      (err) => {
        if (err) throw err;
        res.send({ status: "Success", generatedCode });
      }
    );
  } catch (error) {
    console.error("Error communicating with Ollama:", error);
    res
      .status(500)
      .send({ status: "Error", message: "Failed to generate project." });
  }
});

async function llamaApiCall(prompt) {
  const OLLAMA_API_URL = "http://61.2.142.91:4434/api/chat";
  const HEADERS = { "Content-Type": "application/json" };

  try {
    const response = await axios.post(
      OLLAMA_API_URL,
      {
        model: "llama3.1",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: prompt },
        ],
        stream: false,
      },
      { headers: HEADERS }
    );

    return response.data.message?.content || "Error: Response not available.";
  } catch (error) {
    console.error("Error generating response:", error);
    return "Error generating response";
  }
}

app.post("/generate-project", (req, res) => {
  // Specify the Python script's path
  const pythonScriptPath = path.join(
    __dirname,
    "C:Users\vaibhOneDriveDesktop\vaibhu\vaibhu\backenda.py"
  );

  // Execute the Python script
  exec(`python ${pythonScriptPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send(`Error executing script: ${stderr}`);
    }
    console.log(`stdout: ${stdout}`);
    return res.status(200).send(stdout); // Send back the output of the script
  });
});

app.post("/generate-model", (req, res) => {
  const { moduleName } = req.body;

  // Spawn the Python process and pass the moduleName argument
  const pythonProcess = spawn("python", [
    "C:Users\vaibhOneDriveDesktop\vaibhu\vaibhusrca.py",
    moduleName,
  ]); // Use full path if necessary

  let result = "";

  pythonProcess.stdout.on("data", (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on("close", (code) => {
    if (code === 0) {
      res.json({ message: "Model generation successful!", data: result });
    } else {
      res.status(500).json({ message: "Error generating model." });
    }
  });
});

// Route to handle model generation
app.post("/generate", async (req, res) => {
  const { disease, num_samples, module } = req.body;

  if (!disease || !num_samples || !module) {
    return res
      .status(400)
      .json({ success: false, message: "Missing required parameters" });
  }

  try {
    // Call Ollama API to generate model
    const response = await axios.post(
      OLLAMA_API_URL,
      {
        disease_name: disease,
        num_samples: num_samples,
        module_name: module,
      },
      {
        headers: { Authorization: `Bearer ${OLLAMA_API_KEY}` },
      }
    );

    if (response.data.success) {
      // Returning the generated code and dataset file URL
      return res.json({
        success: true,
        codeContent: response.data.generatedCode,
        dataset: response.data.datasetFileUrl,
      });
    } else {
      return res
        .status(500)
        .json({ success: false, message: "Error generating model" });
    }
  } catch (error) {
    console.error("Ollama API Error:", error);
    return res
      .status(500)
      .json({ success: false, message: "Error calling Ollama API" });
  }
});

// app.post("/run-script", (req, res) => {
//   exec("python sorry_v2.py", (error, stdout, stderr) => {
//       if (error) {
//           console.error(`Error executing script: ${error.message}`);
//           return res.status(500).json({ error: error.message });
//       }
//       if (stderr) {
//           console.error(`Script stderr: ${stderr}`);
//           return res.status(500).json({ error: stderr });
//       }
//       console.log(`Script output: ${stdout}`);
//       res.json({ output: stdout });
//   });
// });
// app.post("/run-script", (req, res) => {
//   const { moduleId } = req.body;
//   if (!moduleId) {
//     return res.status(400).json({ error: "Module ID is required." });
//   }

//   const command = `python codegen.py ${moduleId}`;
//   exec(command, (error, stdout, stderr) => {
//     if (error) {
//       console.error(`Error executing script: ${error.message}`);
//       return res.status(500).json({ error: error.message });
//     }
//     if (stderr) {
//       console.error(`Script stderr: ${stderr}`);
//       return res.status(500).json({ error: stderr });
//     }
//     console.log(`Script output: ${stdout}`);
//     res.json({ output: stdout });
//   });
// });
// app.post("/run-script", (req, res) => {
//   const { module_id, language } = req.body;

//   if (!module_id || !language) {
//       return res.status(400).json({ error: "Module ID and language are required" });
//   }

//   const command = `python3 codegen_groq.py ${module_id} ${language}`;

//   exec(command, (error, stdout, stderr) => {
//       if (error) {
//           console.error(`Error executing script: ${error.message}`);
//           return res.status(500).json({ error: error.message });
//       }
//       if (stderr) {
//           console.error(`Script stderr: ${stderr}`);
//           return res.status(500).json({ error: stderr });
//       }
//       console.log(`Script output: ${stdout}`);
//       res.json({ output: stdout });
//   });
// });

app.post("/run-script", (req, res) => {
  const { module_id, language } = req.body;

  if (!module_id || !language) {
    return res
      .status(400)
      .json({ error: "Module ID and language are required" });
  }

  const command = `python3 codegen_groq_v4.py ${module_id} ${language}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error.message}`);
      return res.status(500).json({ error: error.message });
    }
    if (stderr) {
      console.error(`Script stderr: ${stderr}`);
      return res.status(500).json({ error: stderr });
    }
    console.log(`Script output: ${stdout}`);
    res.json({
      output: stdout,
      filename: `generated_module_${module_id}.${language}`,
    });
  });
});

// app.post("/run-script", (req, res) => {
//   const { module_id, language } = req.body;

//   if (!module_id || !language) {
//     return res.status(400).json({ error: "Module ID and language are required" });
//   }

//   const filename = `generated_module_${module_id}.${language}`;
//   const filePath = path.join(GENERATED_FILES_DIR, filename);
//   const command = `python3 codegen_groq_v2.py ${module_id} ${language}`;

//   exec(command, (error, stdout, stderr) => {
//     if (error) {
//       return res.status(500).json({ error: error.message });
//     }

//     res.json({ output: stdout, filename });
//   });
// });



// // Serve files for download
// app.get("/download-code/:module_id/:language", (req, res) => {
//   const { module_id, language } = req.params;
//   const filePath = path.join(GENERATED_FILES_DIR, `generated_module_${module_id}.${language}`);

//   if (fs.existsSync(filePath)) {
//       res.download(filePath);
//   } else {
//       res.status(404).json({ error: "File not found" });
//   }
// });
// const GENERATED_FILES_DIR = path.join(__dirname, "generated_files");
app.get("/download-code/:module_id/:language", (req, res) => {
  const { module_id, language } = req.params;

  // Get all files matching the module_id and language
  const files = fs.readdirSync(GENERATED_FILES_DIR);
  const matchingFiles = files.filter(
    (file) =>
      file.startsWith(`generated_module_${module_id}_`) &&
      file.endsWith(`.${language}`)
  );

  if (matchingFiles.length === 0) {
    return res.status(404).json({ error: "File not found" });
  }

  // Sort files to get the latest one
  matchingFiles.sort((a, b) => {
    const timestampA = a.match(/\d{8}_\d{6}/);
    const timestampB = b.match(/\d{8}_\d{6}/);
    return timestampB - timestampA; // Latest file first
  });

  const latestFile = matchingFiles[0]; // Get the latest file
  const filePath = path.join(GENERATED_FILES_DIR, latestFile);

  // Set headers to force download and include the correct filename
  res.setHeader("Content-Disposition", `attachment; filename="${latestFile}"`);
  res.setHeader("Content-Type", "application/octet-stream");

  res.download(filePath, latestFile, (err) => {
    if (err) {
      console.error("Error sending file:", err);
      res.status(500).json({ error: "Failed to download file" });
    }
  });
});

// const SELENIUM_FILES_DIR = path.join(GENERATED_FILES_DIR, "selenium");

// app.use(express.static(GENERATED_FILES_DIR));

// // Endpoint to download QA (Selenium) script
// app.get("/download-qa-script/:moduleId", (req, res) => {
//   const { moduleId } = req.params;
//   const filePath = path.join(SELENIUM_FILES_DIR, `selenium_test.py`);

//   res.download(filePath, `qa_script_${moduleId}.py`, (err) => {
//     if (err) {
//       res.status(500).send("Error downloading the file.");
//     }
//   });
// });
const SELENIUM_FILES_DIR = path.join(GENERATED_FILES_DIR, "selenium");
app.use(express.static(GENERATED_FILES_DIR));

// Endpoint to download the latest Selenium script for a module
app.get("/download-qa-script/:moduleId", (req, res) => {
  const { moduleId } = req.params;

  // Get all Selenium test files for this module
  const files = fs.readdirSync(SELENIUM_FILES_DIR);
  const matchingFiles = files.filter(
    (file) =>
      file.startsWith(`selenium_test_${moduleId}_`) && file.endsWith(".py")
  );

  if (matchingFiles.length === 0) {
    return res.status(404).json({ error: "QA script not found" });
  }

  // Sort files to get the latest one based on timestamp
  matchingFiles.sort((a, b) => {
    const timestampA = a.match(/\d{8}_\d{6}/);
    const timestampB = b.match(/\d{8}_\d{6}/);
    return timestampB - timestampA; // Sort in descending order
  });

  const latestFile = matchingFiles[0]; // Get the most recent file
  const filePath = path.join(SELENIUM_FILES_DIR, latestFile);

  // Set proper headers for downloading
  res.setHeader("Content-Disposition", `attachment; filename="${latestFile}"`);
  res.setHeader("Content-Type", "application/octet-stream");

  res.download(filePath, latestFile, (err) => {
    if (err) {
      console.error("Error sending file:", err);
      res.status(500).json({ error: "Failed to download file" });
    }
  });
});

async function llamaApiCall(prompt) {
  const OLLAMA_API_URL = "http://61.2.142.91:4434/api/chat";
  const HEADERS = { "Content-Type": "application/json" };

  console.log("Sending request to Ollama API with prompt:", prompt);
  try {
    const response = await axios.post(
      OLLAMA_API_URL,
      {
        model: "llama3.2",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: prompt },
        ],
        stream: false,
      },
      { headers: HEADERS }
    );

    console.log("Ollama API response received:", response.data);
    return response.data.message?.content || "Error: Response not available.";
  } catch (error) {
    console.error("Error generating response:", error);
    return "Error generating response";
  }
}

app.post("/generate-module", async (req, res) => {
  const { moduleName } = req.body;

  if (!moduleName) {
    return res.status(400).json({ error: "Module name is required" });
  }

  try {
    // Generate SQL Schema using Ollama AI
    const prompt = `Generate a SQL schema for a table to store information about ${moduleName}. Include fields like id, name, description, created_at, and updated_at.`;
    const generatedSQL = await llamaApiCall(prompt);

    if (!generatedSQL) {
      return res.status(500).json({ error: "Failed to generate SQL schema" });
    }

    console.log("Generated SQL:", generatedSQL);

    // Insert module into AIA_MODULES_CODEGEN table
    const insertSQL = `INSERT INTO AIA_MODULES_CODEGEN (module_name, module_description, created_at) VALUES (?, ?, NOW())`;

    db.query(
      insertSQL,
      [`${moduleName}_module`, `Module for ${moduleName}`],
      (err, result) => {
        if (err) {
          console.error("Database Insert Error:", err);
          return res.status(500).json({ error: "Failed to store module" });
        }
        res.json({ message: "Module stored successfully", generatedSQL });
      }
    );
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.use(express.json()); // Middleware to parse JSON request body

app.post("/api/generate-insert", async (req, res) => {
  const { prompt } = req.body;

  console.log("Received request to generate SQL insert statement.");

  if (!prompt) {
    console.log("Error: Prompt is missing.");
    return res.status(400).json({ error: "Prompt is required" });
  }

  const HEADERS = { "Content-Type": "application/json" };
  const finalPrompt = `Generate an INSERT statement for: ${prompt}`;

  console.log("Sending request to Ollama API with prompt:", finalPrompt);

  try {
    const response = await axios.post(
      OLLAMA_API_URL,
      {
        model: "llama3.2",
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: finalPrompt },
        ],
        stream: false,
      },
      { headers: HEADERS }
    );

    console.log("Ollama API response received:", response.data);

    // Check if the response contains the expected data
    if (response.data.message && response.data.message.content) {
      console.log("Generated SQL:", response.data.message.content);
      return res.json({ sql: response.data.message.content });
    } else {
      console.log("Error: Response content not available.");
      return res.json({ sql: "Error: Response not available." });
    }
  } catch (error) {
    console.error("Error with Ollama API:", error.message);
    console.error("Error details:", error.stack);
    return res.status(500).json({ error: "Error generating SQL query" });
  }
});

app.get("/get-sql-data", (req, res) => {
  const sqlData = `INSERT INTO AIA_MODULES_CODEGEN (ID, NAME, MODULE_TYPE, SYMPTOMS, SEVERITY, TREATMENT)
  VALUES
    (1, 'General Information', 'INFO', NULL, NULL, NULL),
    (2, 'Contact Details', 'CONTACT', 'Name', 'Full Name', 'Address'),
    (3, 'Symptoms and Diagnosis', 'DIAGNOSIS', 'Body aches', 'Moderate to Severe', 'Pain Management'),
    (4, 'Treatment Options', 'TREATMENT', 'Medication', 'Mild to Moderate', 'Antibiotics'),
    (5, 'Emergency Contacts', 'CONTACT', 'Family Doctor', 'Primary Care Physician', 'Hospital Name'),
    (6, 'Allergies and Medical History', 'MEDICAL_HISTORY', NULL, NULL, NULL),
    (7, 'Current Medications', 'MEDIATION', NULL, NULL, NULL),
    (8, 'Dietary Restrictions', 'DIETARY_RESTR', NULL, NULL, NULL),
    (9, 'Medication Administration', 'MED_ADMIN', NULL, NULL, NULL);`;

  res.json({ sqlData: sqlData });
});

// app.listen(5001, () => {
//   console.log('Server running on port 5001');
// });

const PORT = 4051; // New port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
