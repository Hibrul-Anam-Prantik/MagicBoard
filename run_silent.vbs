Set WshShell = CreateObject("WScript.Shell")
' Launch Python without showing a window 
WshShell.Run "python Magician.py", 0, False