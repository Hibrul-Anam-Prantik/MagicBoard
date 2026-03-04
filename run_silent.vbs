Set WshShell = CreateObject("WScript.Shell")
' IMPORTANT: The Python script is now named 'clipboard_hotkeys.py'
' The '0' hides the window, 'False' means don't wait for the script to finish.
WshShell.Run "python ghost.py", 0, False