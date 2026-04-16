# Quick Start Guide

## 🚀 How to Run the Application

### Method 1: Double-Click (Easiest)
1. Go to: `c:\Users\Arun Arya\Downloads`
2. **Double-click `run.bat`**
3. Wait for the server to start (you'll see "Running on http://0.0.0.0:5000")
4. Open your browser and go to: **http://localhost:5000**

### Method 2: PowerShell
1. Open PowerShell in the Downloads folder
2. Run: `.\run.ps1`
3. Open browser: **http://localhost:5000**

### Method 3: Manual Steps
```powershell
# Navigate to project folder
cd "c:\Users\Arun Arya\Downloads"

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies (first time only)
pip install -r requirements.txt

# Run the application
python app.py
```

Then open: **http://localhost:5000**

## 📝 What You'll See

After running, you should see:
```
✅ Model loaded successfully from: [path]
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

## 🌐 Access the Application

Open your web browser and visit:
- **http://localhost:5000**
- Or **http://127.0.0.1:5000**

## ⚠️ Troubleshooting

**If you see "Model not found":**
- Copy your `mask_mobilenetv2.h5` file to the Downloads folder
- The app will still run, but predictions won't work without the model

**If port 5000 is busy:**
- Close other applications using port 5000
- Or modify `app.py` line 153 to use a different port (e.g., `port=5001`)

**If dependencies fail to install:**
- Make sure Python is installed: `python --version`
- Try: `python -m pip install --upgrade pip`
- Then: `pip install -r requirements.txt`

## 🛑 To Stop the Server

Press `Ctrl+C` in the command window

