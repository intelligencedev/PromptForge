@echo off
REM PromptForge Server Startup Script (Windows)
REM This script will automatically set up and run the PromptForge server

echo.
echo ============================================
echo    PromptForge - Starting up...
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3 from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
    
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    
    echo [OK] Virtual environment created
    echo.
)

REM Activate virtual environment
echo [SETUP] Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if requirements are installed
if not exist "venv\.requirements_installed" (
    echo.
    echo [SETUP] Installing dependencies...
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    if errorlevel 1 (
        echo [ERROR] Failed to install requirements.
        pause
        exit /b 1
    )
    
    REM Mark requirements as installed
    type nul > venv\.requirements_installed
    echo [OK] Dependencies installed
    echo.
) else (
    echo [OK] Dependencies already installed
    echo.
)

REM Start the Flask server
echo.
echo ============================================
echo   PromptForge is running!
echo   Open your browser and go to:
echo.
echo     http://localhost:5000
echo.
echo   Press Ctrl+C to stop the server
echo ============================================
echo.

python app.py

pause
