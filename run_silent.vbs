Set WshShell = CreateObject("WScript.Shell")
' Ensure the filename matches your Python file exactly
WshShell.Run "python Magician.py", 0, False