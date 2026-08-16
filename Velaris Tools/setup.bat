@echo off
Title Velaris Tools - Setup by Izuki
color 0C

echo.
echo ==================================================
echo              VELARIS TOOLS - SETUP
echo                   made by Izuki
echo ==================================================
echo.

echo [1/5] Checking Python...
where python >nul 2>&1
if errorlevel 1 (
    echo     [FAIL] Python is not installed or not in PATH.
    echo            Install it from: https://python.org/downloads
    echo.
    pause
    exit /b 1
)
for /f "delims=" %%v in ('python --version 2^>^&1') do set "PYVER=%%v"
echo     [OK]   %PYVER%

echo.
echo [2/5] Checking pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo     [FAIL] pip is not available.
    echo.
    pause
    exit /b 1
)
echo     [OK]   pip available

echo.
echo [3/5] Creating virtual environment...
if exist ".venv\Scripts\activate.bat" (
    echo     [OK]   .venv already exists
) else (
    python -m venv .venv
    if errorlevel 1 (
        echo     [FAIL] Could not create the virtual environment.
        echo.
        pause
        exit /b 1
    )
    echo     [OK]   .venv created
)

call ".venv\Scripts\activate.bat"

echo.
echo [4/5] Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo     [OK]   pip upgraded

echo.
echo [5/5] Installing requirements...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo     [FAIL] Failed to install requirements.
    echo.
    pause
    exit /b 1
)
echo     [OK]   Requirements installed

echo.
echo --------------------------------------------------
echo Checking Nmap (required by the tool)...
where nmap >nul 2>&1
if errorlevel 1 (
    echo     [WARN] Nmap was NOT found in PATH.
    echo            Velaris Tools NEEDS Nmap to work.
    echo.
    echo            Download Nmap here: https://nmap.org/download.html
    echo            After installing, RERUN this setup.
) else (
    for /f "delims=" %%n in ('nmap -V 2^>^&1 ^| findstr /i "Nmap version"') do echo     [OK]   %%n
)

echo.
echo ==================================================
echo   Setup complete!
echo.
echo   Run the tool with:
echo       .venv\Scripts\python main.py
echo ==================================================
echo.
pause