@echo off

python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo ERROR: Python is not installed.
    set /p "openWebsite=Do you want to open the Python Website? (y/n): "
    if /i "%openWebsite%"=="y" (
        start https://www.python.org/downloads/
    )
    exit /b 1
)

color 0A
python src/main.py