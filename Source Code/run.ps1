# PowerShell script to run the application
if (-not (Test-Path .venv)) {
    Write-Host "Creating virtual environment with Python 3.10..." -ForegroundColor Yellow
    py -3.10 -m venv .venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Green
& .\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Starting Flask application..." -ForegroundColor Green
python app.py

