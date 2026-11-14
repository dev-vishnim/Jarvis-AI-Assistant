@echo off
cd /d "%~dp0"
py jarvis.py
if errorlevel 1 (
  echo.
  echo JARVIS closed with an error. Review the message above.
  pause
)
