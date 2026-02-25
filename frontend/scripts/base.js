// Adjust the API endpoint to match your Flask backend
const API_URL = '/api/upload'; // Using the base64 endpoint
// const API_URL = '/upload-simple'; // Alternative simpler endpoint

const form = document.getElementById('uploadForm');
const fileInput = document.getElementById('fileInput');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const file = fileInput.files[0];
    if (!file) {
        showResult('Please select a file first.', true);
        return;
    }

    try {
        const reader = new FileReader();
        
        // Read the file as base64
        const base64Content = await new Promise((resolve, reject) => {
            reader.onload = () => resolve(reader.result);
            reader.onerror = () => reject(new Error('Failed to read file'));
            reader.readAsDataURL(file);
        });

        // Prepare JSON payload
        const payload = {
            filename: file.name,
            content: base64Content.split(',')[1] // Remove the data URL prefix
        };

        // Send as JSON
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (!response.ok) {
            throw new Error(`Server responded with status ${response.status}`);
        }
        
        const data = await response.json();
        console.log(data)

        // Check for error response
        if (data.status == 'error') {
            showResult(`Error: ${data.data.message}`, true);
        } else if (data.status == 'success') {
            showResult(`Total words: ${data.data.word_count}`);
        } else {
            showResult('Unexpected response format.', true);
        }
    } catch (error) {
        console.error('Upload error:', error);
        showResult('An error occurred while uploading the file. Please try again.', true);
    }
});



/**
 * Display a message in the result area.
 * @param {string} message - The message to display.
 * @param {boolean} [isError=false] - Whether the message is an error.
 */
function showResult(message, isError = false) {
    resultDiv.textContent = message;
    resultDiv.classList.toggle('error', isError);
}