import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import axios from "axios";
import { ClipLoader } from "react-spinners";
import "./App.css"; // Add your styles here

function App() {
  return (
    <Router basename="/codegen"> {/* Set base path */}
    </Router>
  );
}

// export default App;

// Backend URL for SQL generation
const BACKEND_URL = "http://61.2.142.91:4051/api/generate-insert";

// API call to backend for generating SQL insert statement
async function llamaApiCall(prompt) {
  try {
    const response = await axios.post(BACKEND_URL, { prompt });
    console.log("Backend Response:", response.data); // Debugging
    return response.data.sql || "Error: Response not available.";
  } catch (error) {
    console.error(
      "Error with backend API:",
      error.response ? error.response.data : error.message
    );
    throw new Error("Error generating SQL query");
  }
}

// API call for disease model generator
const API_URL = "http://61.2.142.91:4051";
const generateDiseaseModel = async (prompt) => {
  try {
    const response = await fetch(
      "http://61.2.142.91:4051/api/generate-insert",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      }
    );
    const data = await response.json();
    return data.generatedSQL; // Adjust according to API response
  } catch (error) {
    console.error("Error calling Ollama API:", error);
    return null;
  }
};

const GenerateInsertStatement = () => {
  const [userPrompt, setUserPrompt] = useState("");
  const [sqlQuery, setSqlQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Assuming llamaApiCall is defined somewhere else to make the API call
  const llamaApiCall = async (prompt) => {
    // Make API call to your backend to generate SQL based on the prompt
    // Here we're simulating it with a dummy response
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(
          `INSERT INTO example_table (column1, column2) VALUES ('value1', 'value2');`
        );
      }, 1000);
    });
  };

  const handleGenerateInsert = async () => {
    setLoading(true);
    setError("");

    const defaultPrompt = `Generate an INSERT INTO SQL statement based on the user input. Example:

    INSERT INTO table_name (column1, column2, column3) VALUES ('value1', 'value2', 'value3');
    
    If the user provides specific table names and values, generate the corresponding SQL.`;

    const finalPrompt = userPrompt.trim()
      ? `Generate an INSERT statement for: ${userPrompt}`
      : defaultPrompt;

    try {
      const generatedSql = await llamaApiCall(finalPrompt);
      setSqlQuery(generatedSql);
    } catch (error) {
      console.error("Error generating INSERT statement:", error);
      setError("Error generating SQL. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <textarea
        className="input-textarea"
        value={userPrompt}
        onChange={(e) => setUserPrompt(e.target.value)}
        placeholder="Enter table name and values for INSERT statement"
        rows={4}
        cols={50}
      />
      <br />
      <button
        className="generate-button"
        onClick={handleGenerateInsert}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate INSERT Statement"}
      </button>
      <br />
      {error && <p className="error-text">{error}</p>}
      {sqlQuery && (
        <div className="generated-code-box">
          <h4>Generated SQL:</h4>
          <pre className="output-text">{sqlQuery}</pre>
        </div>
      )}
    </div>
  );
};

const DiseaseModelGenerator = () => {
  const [projects, setProjects] = useState([]);
  const [state, setState] = useState("");
  const [modules, setModules] = useState([]);
  const [error, setError] = useState("");
  const [selectedProject, setSelectedProject] = useState(null);
  const [disease, setDisease] = useState("");
  const [numSamples, setNumSamples] = useState(100);
  const [messages, setMessages] = useState([]);
  const [generatedCode, setGeneratedCode] = useState("");
  const [datasetFile, setDatasetFile] = useState("");
  const [executionStatus, setExecutionStatus] = useState("");
  const [executionOutput, setExecutionOutput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [copyStatus, setCopyStatus] = useState("");
  const [history, setHistory] = useState([]);
  const [description, setDescription] = useState("");
  const [projectName, setProjectName] = useState("");
  const [output, setOutput] = useState("");

  const handleDiseaseModelGeneration = async () => {
    setIsLoading(true);
    setError("");

    const prompt = `Generate a disease prediction model for ${disease} using ${numSamples} samples. Include data processing and machine learning steps.`;
    try {
      const generatedModel = await generateDiseaseModel(prompt);
      setGeneratedCode(generatedModel);
    } catch (error) {
      console.error("Error generating disease model:", error);
      setError("Error generating model. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  //   const runScript = async () => {
  //     try {
  //         const response = await fetch("http://localhost:5001/run-script", {
  //             method: "POST",
  //             headers: {
  //                 "Content-Type": "application/json",
  //             },
  //         });
  //         const data = await response.json();
  //         if (response.ok) {
  //             setOutput(data.output);
  //             setError(null);
  //         } else {
  //             setError(data.error);
  //             setOutput("");
  //         }
  //     } catch (err) {
  //         setError("Failed to connect to server");
  //         setOutput("");
  //     }
  // };
  // const runScript = async (moduleId) => {
  //   try {
  //       const response = await fetch("http://localhost:5001/run-script", {
  //           method: "POST",
  //           headers: {
  //               "Content-Type": "application/json",
  //           },
  //           body: JSON.stringify({ moduleId }), // Send selected module ID
  //       });

  //       const data = await response.json();
  //       if (response.ok) {
  //           setOutput(data.output);
  //           setError(null);
  //       } else {
  //           setError(data.error);
  //           setOutput("");
  //       }
  //   } catch (err) {
  //       setError("Failed to connect to server");
  //       setOutput("");
  //   }
  // };
  const [loading, setLoading] = useState(false);
  const runScript = async (moduleId) => {
    try {
      // Find the selected language (first selected one)
      const selectedLanguage = Object.keys(selectedLanguages).find(
        (lang) => selectedLanguages[lang]
      );

      if (!selectedLanguage) {
        setError("Please select a programming language.");
        return;
      }
      setLoading(true); // Start loading


      const response = await fetch("http://61.2.142.91:4051/run-script", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          module_id: moduleId,
          language: selectedLanguage,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        setOutput(data.output);
        setError(null);
      } else {
        setError(data.error);
        setOutput("");
      }
    } catch (err) {
      setError("Failed to connect to server");
      setOutput("");
    } finally {
      setLoading(false); // Stop loading
    }
  };
  // const runScript = async (moduleId) => {
  //   try {
  //     // Find the selected language
  //     const selectedLanguage = Object.keys(selectedLanguages).find(
  //       (lang) => selectedLanguages[lang]
  //     );

  //     if (!selectedLanguage) {
  //       setError("Please select a programming language.");
  //       return;
  //     }

  //     // Step 1: Call the backend to run the script
  //     const response = await fetch("http://61.2.142.91:4051/run-script", {
  //       method: "POST",
  //       headers: { "Content-Type": "application/json" },
  //       body: JSON.stringify({ module_id: moduleId, language: selectedLanguage }),
  //     });

  //     const data = await response.json();

  //     if (!response.ok) {
  //       setError(data.error);
  //       return;
  //     }

  //     // Step 2: Fetch the generated code file
  //     const codeResponse = await fetch(`http://61.2.142.91:4051/generated-code/${data.filename}`);
  //     const codeText = await codeResponse.text();

  //     if (!codeResponse.ok) {
  //       setError("Failed to fetch generated code.");
  //       return;
  //     }

  //     // Step 3: Update state to display the generated code
  //     setGeneratedCode(codeText);
  //     setError(null);
  //   } catch (err) {
  //     setError("Failed to connect to server");
  //   }
  // };




  // const downloadCode = async (moduleId, language) => {
  //   try {
  //     const fileUrl = `http://61.2.142.91:4051/download-code/${moduleId}/${language}`;
  //     const response = await fetch(fileUrl);

  //     if (!response.ok) {
  //       throw new Error("File not found");
  //     }

  //     // Create a temporary link to trigger download
  //     const blob = await response.blob();
  //     const link = document.createElement("a");
  //     link.href = window.URL.createObjectURL(blob);
  //     link.download = `generated_module_${moduleId}.${language}`;
  //     document.body.appendChild(link);
  //     link.click();
  //     document.body.removeChild(link);
  //   } catch (err) {
  //     console.error("Error downloading file:", err);
  //   }
  // };
  const downloadCode = async (moduleId, language) => {
    try {
      const fileUrl = `http://61.2.142.91:4051/download-code/${moduleId}/${language}`;
      const response = await fetch(fileUrl);

      if (!response.ok) {
        throw new Error("File not found");
      }

      // Extract filename from Content-Disposition header
      const contentDisposition = response.headers.get("Content-Disposition");
      let filename = `generated_module_${moduleId}.${language}`; // Default fallback

      if (contentDisposition) {
        const match = contentDisposition.match(/filename="(.+)"/);
        if (match && match[1]) {
          filename = match[1];
        }
      }

      // Create a temporary link to trigger download
      const blob = await response.blob();
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (err) {
      console.error("Error downloading file:", err);
    }
  };



  // const downloadQAScript = (moduleId) => {
  //   window.location.href = `http://61.2.142.91:4051/download-qa-script/${moduleId}`;
  // };
  const downloadQAScript = async (moduleId) => {
    try {
      const fileUrl = `http://61.2.142.91:4051/download-qa-script/${moduleId}`;
      const response = await fetch(fileUrl);

      if (!response.ok) {
        throw new Error("QA script not found");
      }

      // Extract filename from Content-Disposition header
      const contentDisposition = response.headers.get("Content-Disposition");
      let filename = `qa_script_${moduleId}.py`; // Default fallback

      if (contentDisposition) {
        const match = contentDisposition.match(/filename="(.+)"/);
        if (match && match[1]) {
          filename = match[1];
        }
      }

      // Create a temporary link to trigger download
      const blob = await response.blob();
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (err) {
      console.error("Error downloading QA script:", err);
    }
  };



  const handleGenerateDiseaseModule = async () => {
    if (!disease.trim()) {
      alert("Please enter a disease name.");
      return;
    }

    const prompt = `Generate a SQL schema for a table to store information about ${disease}. Include fields like id, name, symptoms, severity, and treatment.`;
    const generatedSQL = await llamaApiCall(prompt);

    console.log("Generated SQL:", generatedSQL);

    const insertSQL = `
    INSERT INTO AIA_MODULES_CODEGEN (module_name, module_description, created_at)
    VALUES ('${disease}_module', 'Module for ${disease}', NOW());
  `;

    console.log("Insert SQL:", insertSQL);

    // Send insertSQL to the backend (Flask/Node.js) for execution
  };

  const [status, setStatus] = useState({
    dataset: "Not generated",
    code: "Not generated",
    execution: "Not executed yet",
  });

  // handleModify function to modify a selected module
  const handleModify = (moduleName) => {
    setState("Modifying module: " + moduleName);
    // Add logic for modifying the module (like API call or updating state)
  };
  const TextOperations = () => {
    const [text, setText] = useState(""); // Correct hook usage
    return <div>{text}</div>;
  };

  const handleGenerate = async () => {
    try {
      const response = await axios.post(
        "http://61.2.142.91:4051/generate-project",
        {
          description,
          projectName,
        }
      );
      setGeneratedCode(response.data.generatedCode);
    } catch (error) {
      console.error("Error generating project:", error);
    }
  };

  const generateModelForModule = async (moduleName) => {
    console.log(`Generating model for module: ${moduleName}`);
    try {
      const response = await axios.post("http://61.2.142.91:4051/generate", {
        moduleName: moduleName,
      });

      if (response.data.success) {
        setGeneratedCode(response.data.generatedCode);
      } else {
        addMessage("Error generating model.", true);
      }
    } catch (error) {
      console.error("Error generating model:", error);
      addMessage("Error generating model.", true);
    }
  };

  const [modifyDataset, setModifyDataset] = useState([]);
  const [projectData, setProjectData] = useState([]);
  const [showProjectDetails, setShowProjectDetails] = useState(false);
  const [selectedLanguages, setSelectedLanguages] = useState({
    php: false,
    java: false,
    django: false,
  });

  // const toggleLanguage = (language) => {
  //   setSelectedLanguages((prev) => ({
  //     ...prev,
  //     [language]: !prev[language],
  //   }));
  // };
  const toggleLanguage = (language) => {
    setSelectedLanguages({ php: false, java: false, django: false, [language]: true });
  };


  // Fetch Projects
  // useEffect(() => {
  //   fetch("http://localhost:5001/projects")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       if (data.success) {
  //         setProjects(data.data);
  //       } else {
  //         setError("Error fetching projects");
  //       }
  //     })
  //     .catch((err) => {
  //       console.error("Fetch error:", err);
  //       setError("Error fetching projects");
  //     });
  // }, []);
  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const res = await fetch("http://61.2.142.91:4051/projects");
        const data = await res.json();
        if (data.success) {
          setProjects(data.data);
        } else {
          setError("Error fetching projects");
        }
      } catch (err) {
        console.error("Fetch error:", err);
        setError("Error fetching projects");
      }
    };

    fetchProjects();
  }, []);

  // Fetch Modules for selected Project
  const fetchModules = (projectName) => {
    fetch(`http://61.2.142.91:4051/modules?project_name=${projectName}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          setModules(data.data);
          setSelectedProject(projectName);
        } else {
          setModules([]);
          setSelectedProject(null);
          setError("No modules found for this project.");
        }
      })
      .catch((err) => {
        console.error("Fetch error:", err);
        setError("Error fetching modules.");
      });
  };

  // Fetch modules and projects via Axios
  const fetchModulesAndProjects = async () => {
    try {
      const [moduleRes, projectRes] = await Promise.all([
        axios.get(`${API_URL}/api/aia_module`),
        axios.get(`${API_URL}/api/aia_project`),
      ]);
      setModifyDataset(moduleRes.data || []);
      setProjectData(projectRes.data || []);
    } catch (error) {
      addMessage("Error fetching module and project data.", true);
    }
  };

  // Generate Disease Model
  const generateDataAndModel = async () => {
    if (!disease.trim()) {
      addMessage("Please enter a disease name.", true);
      return;
    }
    setStatus((prev) => ({ ...prev, dataset: "Processing..." }));
    setIsLoading(true);
    try {
      const response = await axios.post(`${API_URL}/generate`, {
        disease,
        num_samples: numSamples,
      });
      setGeneratedCode(response.data.codeContent);
      setDatasetFile(response.data.dataset);
      setStatus({
        dataset: "Completed",
        code: "Completed",
        execution: "Not executed yet",
      });
      setHistory((prev) => [...prev, disease]);
      addMessage("Dataset and model generated successfully.", false);
    } catch (error) {
      setStatus((prev) => ({ ...prev, dataset: "Failed" }));
      addMessage("Error generating data and model.", true);
    } finally {
      setIsLoading(false);
    }
  };

  // Add message to the message history
  const addMessage = (text, isError = false) => {
    setMessages((prev) => [...prev, { text, isError }]);
  };

  // Download files (dataset or generated code)
  const downloadFile = async (filename) => {
    if (!filename) {
      alert("No file available to download.");
      return;
    }
    try {
      const response = await axios.get(`${API_URL}/download/${filename}`, {
        responseType: "blob",
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      alert("Error downloading the file.");
    }
  };

  // Execute the generated code
  const executeCode = async () => {
    if (!generatedCode) {
      addMessage("Please generate code before executing.", true);
      return;
    }
    setStatus((prev) => ({ ...prev, execution: "Processing..." }));
    setExecutionOutput("");
    try {
      const response = await axios.post(`${API_URL}/execute`, {
        filename: generatedCode,
      });
      if (response.data.status === "success") {
        setStatus((prev) => ({ ...prev, execution: "Completed" }));
        setExecutionOutput(response.data.output);
      } else {
        setStatus((prev) => ({ ...prev, execution: "Failed" }));
        addMessage(response.data.error || "Unknown error", true);
      }
    } catch (error) {
      setStatus((prev) => ({ ...prev, execution: "Failed" }));
      addMessage("Error executing the code.", true);
    }
  };

  // Copy the generated code to clipboard
  const copyToClipboard = () => {
    if (generatedCode) {
      navigator.clipboard
        .writeText(generatedCode)
        .then(() => setCopyStatus("Copied!"))
        .catch(() => setCopyStatus("Failed to copy."));
    } else {
      setCopyStatus("No code to copy.");
    }
    setTimeout(() => setCopyStatus(""), 2000);
  };

  return (
    <div className="container">
      <header>
        <h1>Codegen</h1>
      </header>
      <div className="chatbox">
        <div className="left-window">
          <h3>Input</h3>
          <input
            type="text"
            value={disease}
            onChange={(e) => setDisease(e.target.value)}
            placeholder="Enter "
          />

          {/* Checkboxes for PHP, Java, and Django */}
          <div className="checkbox-group">
            <label>
              <input
                type="checkbox"
                checked={selectedLanguages.php}
                onChange={() => toggleLanguage("php")}
              />
              PHP
            </label>
            <label>
              <input
                type="checkbox"
                checked={selectedLanguages.java}
                onChange={() => toggleLanguage("java")}
              />
              Java
            </label>
            <label>
              <input
                type="checkbox"
                checked={selectedLanguages.django}
                onChange={() => toggleLanguage("django")}
              />
              Django
            </label>
          </div>

          <div className="button-container">
            <button onClick={handleGenerateDiseaseModule}>
              Generate Disease Module
            </button>

            <button onClick={generateDataAndModel} disabled={isLoading}>
              {isLoading ? "Generating..." : "Generate"}
            </button>
            <button
              onClick={() => downloadFile(datasetFile)}
              disabled={!datasetFile}
            >
              Download Dataset
            </button>
            <button
              onClick={() => downloadFile(generatedCode)}
              disabled={!generatedCode}
            >
              Download Code
            </button>
            <button onClick={executeCode} disabled={!generatedCode}>
              Execute Code
            </button>
            <button onClick={fetchModulesAndProjects}>Modify</button>
            {modifyDataset.length > 0 && (
              <button onClick={() => setShowProjectDetails(true)}>
                Project Details
              </button>
            )}
          </div>

          {modifyDataset.length > 0 && (
            <div className="modify-dataset">
              <h3>Modify MODULE</h3>
              <ul>
                {modifyDataset.map((module, index) => (
                  <li key={index}>{module.module_name}</li>
                ))}
              </ul>
            </div>
          )}

          {showProjectDetails && projectData.length > 0 && (
            <div className="modify-dataset">
              <h3>Project Details</h3>
              <ul>
                {projectData.map((project, index) => (
                  <li key={index}>
                    <strong>Project Name:</strong> {project.PROJECT_NAME}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <div className="status-window">
            <h3>Status</h3>
            <p>
              <strong>Dataset Generated:</strong> {status.dataset}
            </p>
            <p>
              <strong>Code Generated:</strong> {status.code}
            </p>
            <p>
              <strong>Execution Status:</strong> {status.execution}
            </p>
          </div>
        </div>

        {/* Right Window Section (added content) */}
        <div className="right-window">
          <h2>Project List</h2>
          {error && <p style={{ color: "red" }}>{error}</p>}
          <ul>
            {projects.length > 0 ? (
              projects.map((project) => (
                <li key={project.project_id}>
                  {project.project_name}{" "}
                  <button onClick={() => fetchModules(project.project_name)}>
                    Show Modules
                  </button>
                </li>
              ))
            ) : (
              <p>No projects found.</p>
            )}
          </ul>

          {/* {selectedProject && (
            <div>
              <h3>Modules for {selectedProject}</h3>
              <ul>
                {modules.length > 0 ? (
                  modules.map((module, index) => (
                    // const selectedLanguage = Object.keys(selectedLanguages).find(
                    //   (lang) => selectedLanguages[lang]
                    // );
          
                    // return (
                    <li key={index}>
                      {module.module_name}{" "}
                      <button onClick={() => runScript(module.module_id)}>
                        Old
                      </button>
                      <button onClick={() => downloadCode(module.module_id, selectedLanguage)}>Download Code</button>
                      <button onClick={() => createNewModule(module.module_id)}>
                        New
                      </button>
                      <button onClick={() => applyCSS(module.module_id)}>
                        CSS
                      </button>
                      {output && <p>Output: {output}</p>}
                      {error && <p style={{ color: "red" }}>Error: {error}</p>}
                    </li>
                  ))
                ) : (
                  <p>No modules found.</p>
                )}
              </ul>
            </div>
          )} */}
          {selectedProject && (
            <div>
              <h3>Modules for {selectedProject}</h3>
              <ul>
                {modules.length > 0 ? (
                  modules.map((module, index) => {
                    const selectedLanguage = Object.keys(
                      selectedLanguages
                    ).find((lang) => selectedLanguages[lang]);

                    return (
                      <li key={index}>
                        {/* {module.module_name}{" "}
                        <button onClick={() => runScript(module.module_id)}>
                          Generate code
                        </button>
                        <button
                          onClick={() =>
                            downloadCode(module.module_id, selectedLanguage)
                          }
                        >
                          Download Code
                        </button> */}
                        {/* <button
                          onClick={() => createNewModule(module.module_id)}
                        >
                          New
                        </button>
                        <button onClick={() => applyCSS(module.module_id)}>
                          CSS
                        </button> */}
                        {/* <button
                          onClick={() => downloadQAScript(module.module_id)}
                        >
                          Download QA Script
                        </button> */}
                        {module.module_name}{" "}
                        <button onClick={() => runScript(module.module_id)} disabled={loading}>
                          {loading ? <ClipLoader color="#09f" size={20} /> : "Generate Code"}
                        </button>
                        <button
                          onClick={() => downloadCode(module.module_id, selectedLanguage)}
                          disabled={loading}
                        >
                          Download Code
                        </button>
                        <button onClick={() => downloadQAScript(module.module_id)} disabled={loading}>
                          Download QA Script
                        </button>
                        {output && <p>Output: {output}</p>}
                        {error && (
                          <p style={{ color: "red" }}>Error: {error}</p>
                        )}
                      </li>
                    );
                  })
                ) : (
                  <p>No modules found.</p>
                )}
              </ul>
            </div>
          )}
          <div className="code-window">
            <h3>Generated Code</h3>
            <div className="code-container">
              {generatedCode ? (
                <>
                  <button onClick={handleGenerateDiseaseModule}>
                    Generate Disease Module
                  </button>
                  <button onClick={copyToClipboard}>⧉ Copy</button>
                  {copyStatus && (
                    <span className="copy-status">{copyStatus}</span>
                  )}
                  <pre className="code-output">{generatedCode}</pre>
                </>
              ) : (
                <p>No code generated yet.</p>
              //   <>
              //   {/* <button onClick={() => runScript(module.module_id)} disabled={loading}>
              //     {loading ? <ClipLoader color="#09f" size={20} /> : "Generate Code"}
              //   </button> */}
              //   <p>No code generated yet.</p>
              // </>
              )}
            </div>
          </div>

          <div className="message-window">
            <h3>Messages</h3>
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`message ${msg.isError ? "error" : "success"}`}
              >
                {msg.text}
              </div>
            ))}
          </div>

          <div className="execution-output">
            <h3>Execution Output</h3>
            <pre>{executionOutput || "No output yet."}</pre>
          </div>

          <div className="history-window">
            <h3>History</h3>
            <ul>
              {history.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};
export default DiseaseModelGenerator;
