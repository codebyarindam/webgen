// src/api.js
import axios from 'axios';

const API_URL = "http://<button onClick={() => runScript(module.module_id)}>Old</button>:5000";  // Replace with your actual backend URL

export const saveTaskResult = async (taskId, resultStatus, resultData) => {
  try {
    const response = await axios.post(`${API_URL}/save-task-result`, {
      taskId,
      resultStatus,
      resultData
    });
    return response.data;
  } catch (error) {
    throw new Error('Failed to save task result: ' + error.message);
  }
};

export const checkPythonCode = async (userId, diseaseParentId) => {
  try {
    const response = await axios.post(`${API_URL}/check-python-code`, { userId, diseaseParentId });
    return response.data;
  } catch (error) {
    throw new Error('Failed to check Python code: ' + error.message);
  }
};
