import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const TextOperations = () => {
  const [text, setText] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [imagePath, setImagePath] = useState('');
  const [profiles, setProfiles] = useState([]); // State to store fetched profiles
  const [selectedProfile, setSelectedProfile] = useState(null); // Track selected profile
  const [summary, setSummary] = useState('');
  const [generatedText, setGeneratedText] = useState('');
  const [caption, setCaption] = useState('');
  const [title, setTitle] = useState('');
  const [loading, setLoading] = useState(false);
  const [selectedLlm, setSelectedLlm] = useState('');
  const [confirmedLlm, setConfirmedLlm] = useState('');
  const [error, setError] = useState(null);
  const [status, setStatus] = useState({
    summarize: '',
    generate: '',
    caption: '',
    title: ''
  });

 
  const fetchProfiles = async () => {
    try {
      const response = await fetch('http://localhost:4600/get-profiles');
      const data = await response.json();
      if (response.ok) {
        setProfiles(data); // Set fetched profiles
      } else {
        setError('Error fetching profiles');
      }
    } catch (error) {
      setError('Error fetching profiles');
      console.error('Error:', error);
    }
  };

  const handleProfileSelect = (profile) => {
    setSelectedProfile(profile);
    
    // Concatenate all profile data into a string and set it as text input
    const profileData = ` 
      Category: ${profile.category}
      Role: ${profile.role}
      User Input: ${profile.userInput}
      Generated Profile: ${profile.generatedProfile}
      Created At: ${profile.created_at}
      Status: ${profile.status}
    `;

    setText(profileData.trim()); // Trim to remove excess whitespace
  };

  const handleTextChange = (e) => setText(e.target.value);

  const handleLLMSelect = (value) => {
    setSelectedLlm(value);
    setConfirmedLlm(value);
  };

  const handleApiCall = async (endpoint, prompt, setState, taskName) => {
    if (!confirmedLlm) {  // LLM selection check
      alert('Please select an LLM before proceeding.');
      return;
    }
  
    setStatus(prevStatus => ({ ...prevStatus, [taskName]: 'processing' }));
    setLoading(true);
    try {
      const response = await axios.post(`http://localhost:4600/${endpoint}`, { text, llm: confirmedLlm, userId: 919, firmId: 35 });
  
      console.log(response.data); // Log the full response from the backend
      setState(response.data[taskName]);  // Update the state with the backend result
      setStatus(prevStatus => ({ ...prevStatus, [taskName]: 'completed' }));
    } catch (error) {
      console.error(`Error with ${endpoint} endpoint`, error);
      setStatus(prevStatus => ({ ...prevStatus, [taskName]: 'failed' }));
    }
    setLoading(false);
  };
  
  const handleSummarize = () => handleApiCall('summarize', `Summarize the following text in plain text without using numbered bullets or any special formatting: ${text}`, setSummary, 'summarize');
  const handleGenerate = () => handleApiCall('generate', `Generate more content based on the following text: ${text}`, setGeneratedText, 'generate');
  const handleCaption = () => handleApiCall('caption', `Generate a caption for the following text: ${text}`, setCaption, 'caption');
  const handleTitle = () => handleApiCall('title', `Generate a title for the following text: ${text}`, setTitle, 'title');
  

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!text) {
      setError('Text is required!');
      return;
    }

    setError('');
    try {
      setStatus(prevStatus => ({ ...prevStatus, generateImage: 'processing' }));
      const response = await fetch('http://localhost:4600/generate-image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (response.ok) {
        setImageUrl(`http://localhost:4600${data.imageUrl}`);
        setImagePath(data.imageUrl);
        setStatus(prevStatus => ({ ...prevStatus, generateImage: 'completed' }));
      } else {
        setError(data.error || 'Error generating image.');
        setStatus(prevStatus => ({ ...prevStatus, generateImage: 'failed' }));
      }
    } catch (err) {
      console.error('Error:', err);
      setError('Error generating image.');
      setStatus(prevStatus => ({ ...prevStatus, generateImage: 'failed' }));
    }
  };

  return (
    <div>
      <div className="menu-item">
        <h3>Text Operations</h3>

        {/* LLM Selector */}
        <div className="llm-selector">
          <span>Select LLM:</span>
          <select
            value={selectedLlm}
            onChange={(e) => handleLLMSelect(e.target.value)}
            className="llm-dropdown"
          >
           
          
          </select>
        </div>

        <p>Selected LLM: {confirmedLlm}</p>

        <textarea
          value={text}
          onChange={handleTextChange}
          placeholder="Enter text here"
          rows="6"
          cols="50"
        />

        {/* Buttons for text operations */}
        <div className="buttons">
          <button onClick={handleSummarize} disabled={loading}>Summarize</button>
          <button onClick={handleGenerate} disabled={loading}>Generate</button>

          {/* Updated buttons without selectedProfile dependency */}
          <button onClick={handleCaption} disabled={loading}>Generate Caption</button>
          <button onClick={handleTitle} disabled={loading}>Generate Title</button>

          <Link to="/profile-builder">
            <button>Profile Builder</button>
          </Link>
          <Link to="/QA">
            <button>QA</button>
          </Link>
          <button onClick={fetchProfiles}>Show Active Profiles</button>
        </div>

        {loading && <p>Loading...</p>}

        {/* Display Results */}
        <div id="chatbox" className="chatbox">
          <div className="generated-results">
            <div className="result-box">
              <p><strong>Summary:</strong></p>
              <p>{status.summarize === 'processing' ? 'Processing...' : summary}</p>
              <p>Status: {status.summarize}</p>
            </div>

            <div className="result-box">
              <p><strong>Generated Text:</strong></p>
              <p>{status.generate === 'processing' ? 'Processing...' : generatedText}</p>
              <p>Status: {status.generate}</p>
            </div>

            <div className="result-box">
              <p><strong>Generated Caption:</strong></p>
              <p>{status.caption === 'processing' ? 'Processing...' : caption}</p>
              <p>Status: {status.caption}</p>
            </div>

            <div className="result-box">
              <p><strong>Generated Title:</strong></p>
              <p>{status.title === 'processing' ? 'Processing...' : title}</p>
              <p>Status: {status.title}</p>
            </div>

            <div className="result-box">
              <p><strong>Image:</strong></p>
              {imageUrl && <img src={imageUrl} alt="Generated" />}
              <p>Status: {status.generateImage}</p>
            </div>
          </div>
        </div>

        {/* Display active profiles */}
        <div className="active-profiles">
          {profiles.length > 0 ? (
            <ul>
              {profiles.map((profile) => (
                <li key={profile.id} onClick={() => handleProfileSelect(profile)}>
                  <p><strong>Category:</strong> {profile.category}</p>
                  <p><strong>Role:</strong> {profile.role}</p>
                  <p><strong>User Input:</strong> {profile.userInput}</p>
                  <p><strong>Generated Profile:</strong> {profile.generatedProfile}</p>
                  <p><strong>Status:</strong> {profile.status}</p>
                  <p><strong>Created At:</strong> {profile.created_at}</p>
                  <hr />
                </li>
              ))}
            </ul>
          ) : (
            <p>No active profiles found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default TextOperations;
