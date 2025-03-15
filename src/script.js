// // Final~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// // // Define backend API endpoints
// const API_URL = "http://127.0.0.1:5000"; // Update if the Flask server runs on a different host/port

// // Get references to DOM elements
// const diseaseInput = document.getElementById("diseaseInput");
// const generateButton = document.getElementById("generateButton");
// const downloadDatasetButton = document.getElementById("downloadDatasetButton");
// const downloadCodeButton = document.getElementById("downloadCodeButton");
// const chatbox = document.getElementById("chatbox");

// // Store file names for downloading
// let datasetFilename = "";
// let codeFilename;

// // Function to display messages in the chatbox
// function displayMessage(message, isError = false) {
//     const messageElement = document.createElement("p");
//     messageElement.textContent = message;
//     messageElement.className = isError ? "error-message" : "success-message";
//     chatbox.appendChild(messageElement);
//     chatbox.scrollTop = chatbox.scrollHeight;
// }

// // Event listener for "Generate" button
// generateButton.addEventListener("click", async () => {
//     const diseaseName = diseaseInput.value.trim();
//     if (!diseaseName) {
//         displayMessage("Please enter a disease name.", true);
//         return;
//     }

//     displayMessage(`Generating data and model for '${diseaseName}'...`);

//     try {
//         // Make a POST request to the backend
//         const response = await fetch(`${API_URL}/generate`, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({ disease: diseaseName }),
//         });

//         if (!response.ok) {
//             const errorData = await response.json();
//             displayMessage(errorData.error || "Failed to generate data and model.", true);
//             return;
//         }

//         const data = await response.json();
//         datasetFilename = data.dataset;
//         codeFilename = data.code;

//         displayMessage("Dataset and model generated successfully.");
//         downloadDatasetButton.disabled = false;
//         downloadCodeButton.disabled = false;
//     } catch (error) {
//         console.error("Error:", error);
//         displayMessage("An error occurred while generating data and model.", true);
//     }
// });

// // Event listener for "Download Dataset" button
// downloadDatasetButton.addEventListener("click", () => {
//     if (datasetFilename) {
//         window.open(`${API_URL}/download/${datasetFilename}`, "_blank");
//     } else {
//         displayMessage("No dataset available for download.", true);
//     }
// });

// // Event listener for "Download Code" button
// downloadCodeButton.addEventListener("click", () => {
//     if (codeFilename) {
//         window.open(`${API_URL}/download/${codeFilename}`, "_blank");
//     } else {
//         displayMessage("No code available for download.", true);
//     }
// });




// document.getElementById('generateButton').addEventListener('click', async () => {
//     const disease = document.getElementById('disease').value;
//     const params = document.getElementById('params').value;
//     const numSamples = document.getElementById('samples').value;

//     if (!disease || !params) {
//         alert('Please enter all the required fields!');
//         return;
//     }

//     try {
//         const response = await fetch('http://localhost:5000/generate', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({
//                 disease: disease,
//                 params: params.split(','),
//                 num_samples: parseInt(numSamples),
//             }),
//         });

//         if (!response.ok) {
//             throw new Error(`Server error: ${response.statusText}`);
//         }

//         const data = await response.json();

//         const outputDiv = document.getElementById('output');
//         outputDiv.innerHTML = `
//             <p><strong>Files Generated:</strong></p>
//             <a href="http://localhost:5000/download/${data.dataset}" target="_blank">Download Dataset</a><br>
//             <a href="http://localhost:5000/download/${data.code}" target="_blank">Download Code</a>
//         `;
//     } catch (error) {
//         alert(`Error: ${error.message}`);
//     }
// });




// // Backend API base URL
// const API_URL = "http://127.0.0.1:5000"; // Update if Flask server runs on a different host/port

// // Get references to DOM elements
// const diseaseInput = document.getElementById("diseaseInput");
// const generateButton = document.getElementById("generateButton");
// const downloadDatasetButton = document.getElementById("downloadDatasetButton");
// const downloadCodeButton = document.getElementById("downloadCodeButton");
// const executeCodeButton = document.getElementById("executeCodeButton"); // New
// const chatbox = document.getElementById("chatbox");

// // Store file names for downloading and execution
// let datasetFilename = "";
// let codeFilename = "";

// // Function to display messages in the chatbox
// // function displayMessage(message, isError = false) {
// //     const messageElement = document.createElement("p");
// //     messageElement.textContent = message;
// //     messageElement.className = isError ? "error-message" : "success-message";
// //     chatbox.appendChild(messageElement);
// //     chatbox.scrollTop = chatbox.scrollHeight;
// // }
// function displayMessage(message, isError = false) {
//     const messageElement = document.createElement("p");
//     messageElement.textContent = message;
//     messageElement.className = isError ? "error-message" : "success-message";
//     const chatbox = document.getElementById("chatbox");
//     chatbox.appendChild(messageElement);
//     chatbox.scrollTop = chatbox.scrollHeight;
// }


// // Event listener for "Generate" button
// generateButton.addEventListener("click", async () => {
//     const diseaseName = diseaseInput.value.trim();
//     if (!diseaseName) {
//         displayMessage("Please enter a disease name.", true);
//         return;
//     }

//     displayMessage(`Generating data and model for '${diseaseName}'...`);

//     try {
//         // Make a POST request to the backend
//         const response = await fetch(`${API_URL}/generate`, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({ disease: diseaseName }),
//         });

//         if (!response.ok) {
//             const errorData = await response.json();
//             displayMessage(errorData.error || "Failed to generate data and model.", true);
//             return;
//         }

//         const data = await response.json();
//         datasetFilename = data.dataset;
//         codeFilename = data.code;

//         displayMessage("Dataset and model generated successfully.");
//         downloadDatasetButton.disabled = false;
//         downloadCodeButton.disabled = false;
//         executeCodeButton.disabled = false; // Enable Execute button
//     } catch (error) {
//         console.error("Error:", error);
//         displayMessage("An error occurred while generating data and model.", true);
//     }
// });

// // Event listener for "Download Dataset" button
// downloadDatasetButton.addEventListener("click", () => {
//     if (datasetFilename) {
//         window.open(`${API_URL}/download/${datasetFilename}`, "_blank");
//     } else {
//         displayMessage("No dataset available for download.", true);
//     }
// });

// // Event listener for "Download Code" button
// downloadCodeButton.addEventListener("click", () => {
//     if (codeFilename) {
//         window.open(`${API_URL}/download/${codeFilename}`, "_blank");
//     } else {
//         displayMessage("No code available for download.", true);
//     }
// });

// // Event listener for "Execute Code" button
// executeCodeButton.addEventListener("click", async () => {
//     if (!codeFilename) {
//         displayMessage("No code available to execute.", true);
//         return;
//     }

//     displayMessage(`Executing the code '${codeFilename}'...`);

//     try {
//         // Make a POST request to the backend for code execution
//         const response = await fetch(`${API_URL}/execute`, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({ filename: codeFilename }),
//         });

//         const result = await response.json();

//         if (response.ok && result.status === "success") {
//             displayMessage("Code executed successfully. Output:");
//             displayMessage(result.output);
//         } else {
//             displayMessage("Error during code execution:", true);
//             displayMessage(result.error, true);
//         }
//     } catch (error) {
//         console.error("Error executing code:", error);
//         displayMessage("An error occurred while executing the code.", true);
//     }
// });








// Backend API base URL
const API_URL = "http://127.0.0.1:5000"; // Update if Flask server runs on a different host/port

// Get references to DOM elements
const diseaseInput = document.getElementById("diseaseInput");
const generateButton = document.getElementById("generateButton");
const downloadDatasetButton = document.getElementById("downloadDatasetButton");
const downloadCodeButton = document.getElementById("downloadCodeButton");
const executeCodeButton = document.getElementById("executeCodeButton"); // New
const chatbox = document.getElementById("chatbox");

// Store file names for downloading and execution
let datasetFilename = "";
let codeFilename = "";

// Function to display messages in the chatbox
// function displayMessage(message, isError = false) {
//     const messageElement = document.createElement("p");
//     messageElement.textContent = message;
//     messageElement.className = isError ? "error-message" : "success-message";
//     chatbox.appendChild(messageElement);
//     chatbox.scrollTop = chatbox.scrollHeight;
// }
function displayMessage(message, isError = false) {
    console.log("displayMessage called:", message); // Log to see if this function is being called
    const messageElement = document.createElement("p");
    messageElement.textContent = message;
    messageElement.className = isError ? "error-message" : "success-message";
    const chatbox = document.getElementById("chatbox");
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}


// Event listener for "Generate" button
generateButton.addEventListener("click", async () => {
    const diseaseName = diseaseInput.value.trim();
    if (!diseaseName) {
        displayMessage("Please enter a disease name.", true);
        return;
    }

    displayMessage(`Generating data and model for '${diseaseName}'...`);

    try {
        // Make a POST request to the backend
        const response = await fetch(`${API_URL}/generate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ disease: diseaseName }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            displayMessage(errorData.error || "Failed to generate data and model.", true);
            return;
        }

        const data = await response.json();
        datasetFilename = data.dataset;
        codeFilename = data.code;

        displayMessage("Dataset and model generated successfully.");
        downloadDatasetButton.disabled = false;
        downloadCodeButton.disabled = false;
        executeCodeButton.disabled = false; // Enable Execute button
    } catch (error) {
        console.error("Error:", error);
        displayMessage("An error occurred while generating data and model.", true);
    }
});

// Event listener for "Download Dataset" button
downloadDatasetButton.addEventListener("click", () => {
    if (datasetFilename) {
        window.open(`${API_URL}/download/${datasetFilename}`, "_blank");
    } else {
        displayMessage("No dataset available for download.", true);
    }
});

// Event listener for "Download Code" button
downloadCodeButton.addEventListener("click", () => {
    if (codeFilename) {
        window.open(`${API_URL}/download/${codeFilename}`, "_blank");
    } else {
        displayMessage("No code available for download.", true);
    }
});

// Event listener for "Execute Code" button
executeCodeButton.addEventListener("click", async () => {
    if (!codeFilename) {
        displayMessage("No code available to execute.", true);
        return;
    }

    displayMessage(`Executing the code '${codeFilename}'...`);

    try {
        // Make a POST request to the backend for code execution
        const response = await fetch(`${API_URL}/execute`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ filename: codeFilename }),
        });

        const result = await response.json();

        if (response.ok && result.status === "success") {
            displayMessage("Code executed successfully. Output:");
            displayMessage(result.output);
        } else {
            displayMessage("Error during code execution:", true);
            displayMessage(result.error, true);
        }
    } catch (error) {
        console.error("Error executing code:", error);
        displayMessage("An error occurred while executing the code.", true);
    }
});
