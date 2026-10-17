@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
if errorlevel 1 goto fail
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto fail
echo Open http://127.0.0.1:5000 in your browser. Ctrl+C stops the server.
.venv\Scripts\python.exe -m flask --app app run --host 127.0.0.1
goto end
:fail
echo Setup failed. Check that Python 3.10 or 3.11 and internet access are available.
pause
:end
