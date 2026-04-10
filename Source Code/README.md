<<<<<<< HEAD
# Face Mask Detection Web Application

A modern web application for detecting face masks in images using deep learning (MobileNetV2).

## Features

- 🖼️ Image upload (drag & drop or click to select)
- 📷 Real-time camera capture
- 🤖 AI-powered mask detection
- 📊 Confidence score display
- 🎨 Modern, responsive UI

## Setup Instructions

### Option 1: Using Virtual Environment (Recommended)

1. **Create and activate virtual environment:**

   **Windows (PowerShell):**
   ```powershell
   py -3.10 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Windows (Command Prompt):**
   ```cmd
   py -3.10 -m venv .venv
   .venv\Scripts\activate.bat
   ```

   **Linux/Mac:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Place your model file:**
   - Copy your trained model `mask_mobilenetv2.h5` to the project root directory
   - The model should be in the same folder as `app.py`

4. **Run the application:**
   
   **Windows - Quick Start:**
   - Double-click `run.bat` (Command Prompt) or run `.\run.ps1` (PowerShell)
   
   **Or manually:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   - Open your browser and go to: `http://localhost:5000`

### Option 2: Without Virtual Environment

If you prefer not to use a virtual environment, you can install dependencies globally:
```bash
pip install -r requirements.txt
python app.py
```

**Note:** Using a virtual environment is recommended to avoid conflicts with other Python projects.

## Project Structure

```
.
├── app.py                 # Flask backend server
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend JavaScript
├── .venv/                # Virtual environment (created after setup)
├── requirements.txt      # Python dependencies
├── run.bat              # Windows batch script to run app
├── run.ps1              # PowerShell script to run app
├── mask_mobilenetv2.h5   # Trained model (you need to add this)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## API Endpoints

- `GET /` - Main page
- `POST /predict` - Predict mask detection (expects image file)
- `GET /health` - Health check endpoint

## Notes

- The model expects images of size 224x224 pixels
- Supported image formats: PNG, JPG, JPEG, GIF
- Maximum file size: 16MB
=======

# Team Number – Project Title

## Team Info
- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05XX — **Name** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

---

## Abstract
xxxxxxxxxx

---

## Paper Reference (Inspiration)
👉 **[Paper Title xxxxxxxxxx
  – Author Names xxxxxxxxxx
 ](Paper URL here)**
Original conference/IEEE paper used as inspiration for the model.

---

## Our Improvement Over Existing Paper
xxxxxxxxxx

---

## About the Project
Give a simple explanation of:
- What your project does
- Why it is useful
- General project workflow (input → processing → model → output)

---

## Dataset Used
👉 **[Dataset Name](Dataset URL)**

**Dataset Details:**
xxxxxxxxxx

---

## Dependencies Used
xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx ...

---

## EDA & Preprocessing
xxxxxxxxxx

---

## Model Training Info
xxxxxxxxxx

---

## Model Testing / Evaluation
xxxxxxxxxx

---

## Results
xxxxxxxxxx

---

## Limitations & Future Work
xxxxxxxxxx

---

## Deployment Info
xxxxxxxxxx

---
>>>>>>> 0ba72d367da784cb70849d62f31d42e8430464ab
