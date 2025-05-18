import React, { useState } from 'react';

const UploadPage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setUploadStatus('');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        setUploadStatus('Uploading...');
        const response = await fetch('http://127.0.0.1:8000/api/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          setUploadStatus('Upload successful!');
        } else {
          setUploadStatus('Upload failed.');
        }
      } catch (error) {
        setUploadStatus('Upload error.');
      }
    }
  };

  return (
    <div>
      <h2>Upload Audio File</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="audio/*"
          onChange={handleFileChange}
        />
        <button type="submit" disabled={!selectedFile}>
          Upload
        </button>
      </form>
      {selectedFile && (
        <p>Selected file: {selectedFile.name}</p>
      )}
      {uploadStatus && (
        <p>{uploadStatus}</p>
      )}
    </div>
  );
};

export default UploadPage;