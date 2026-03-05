@echo off
cd /d "%~dp0"
wscript.exe run_silent.vbs

:: @echo off
::rem Executes the VBScript, which in turn launches the Python script silently.
::wscript.exe run_silent.vbs