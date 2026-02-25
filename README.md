# Word Counter Application

A lightweight web application built with **Python (Flask)** on the backend and **HTML, CSS, JavaScript** on the frontend.  
Users can upload files through the UI, and the backend processes them to return a JSON response containing the total word count.

---

## ✨ Features
- Upload files via a simple web interface
- Supported formats: `.docx`, `.pdf`, `.csv`, `.txt`
- Backend powered by Flask
- Frontend built with HTML, CSS, and JavaScript
- Returns results as JSON for easy integration
- Basic text cleaning (removes punctuation, converts to lowercase)

---

## 📂 Project Structure
```text
Word-Counter/
│
├── src/
│   ├── app.py              # Flask backend entry point
│   ├── requirements.txt    # Python dependencies
│   ├── file_manager.py
│   └── count_words.py
├── frontend/
│   ├── templates/
│      └── base.html       # Frontend UI
│   ├── scripts/
│      ├── base.css       # CSS styling
│      └── base.js       # JavaScript logic
└── README.md           # Project documentation
```
---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/truthmyson/Word-Counter.git
   cd Word-Counter
   ```
2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies
   ```bash
   pip install -r 'src/requirements.txt'
   ```
   
---
## Usage
1. start the flask backend:
   ```bash
   python 'src/app.py'
2. Open the frontend by runing the base.html file
3. Upload a file and receive a json response
   Example response:
   ```json
       {
        "status": "success",
        "data": {
          "file_name": "example.docx",
          "file_type": "docx",
          "word_count": 523,
          "processed_time": "2026-02-23 14:41:00",
          "response_error": 200
        }
      }
   ```
   
---
## 📸 Screenshots

![App Screenshot](static/ui.png)
---
## 🚀 Running Word Counter with Docker
1. 📥 Pull the Image
   ```bash
   docker pull truthmyson/wordcounter-frontend:latest
   docker pull truthmyson/wordcounter-backend:latest
   ```
2.  ▶️ Run the Containers
    backend (flask Api)
    ```bash
    docker run -d --name wordcounter-backend -p 5000:5000 truthmyson/wordcounter-backend:latest
    ```
    frontend(Nginx)
    ```bash
    docker run -d --name wordcounter-frontend -p 80:80 truthmyson/wordcounter-frontend:latest
    ```
3. ✅ Usage
   open your browser and enter the url
   ```bash
   http://localhost:80
   ```
   or
   ```bash
   http://localhost
   ```
   
NOTE: Make sure both containers are running
```bash
docker ps
```
---
DON'T forget to manually close the the containers because they would be running in detached mood "background".
