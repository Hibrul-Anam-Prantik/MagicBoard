import pynput
import pyperclip
import os
import sys

# File mapping
CLIP_FILES = {
    "1": "magic01.txt", "2": "magic02.txt", "3": "magic03.txt", "4": "magic04.txt",
    "5": "magic05.txt", "6": "magic06.txt", "7": "magic07.txt", "8": "magic08.txt",
}

CLIPS = {}

def load_clips():
    """Reads content from text files into memory"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    for index, filename in CLIP_FILES.items():
        full_path = os.path.join(base_path, filename)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                CLIPS[index] = f.read().strip()
        else:
            CLIPS[index] = "Error: " + filename + " not found."

def trigger_clip(index):
    """Copies text to clipboard"""
    content = CLIPS.get(index, "")
    if not content.startswith("Error:"):
        pyperclip.copy(content)
        print("Copied clip " + index + " to clipboard.")

def kill_script():
    """Stops the background process safely"""
    print("MagicBoard shutting down...")
    os._exit(0)

load_clips()

# Setup Modifiers: 'cmd' for Mac, 'ctrl' for Windows
mod = '<cmd>' if sys.platform == 'darwin' else '<ctrl>'
friendly_mod = "Command" if sys.platform == 'darwin' else "Ctrl"

# Build hotkey dictionary
hotkeys = {}
for i in CLIPS.keys():
    hotkey_str = mod + "+<alt>+" + i
    hotkeys[hotkey_str] = lambda idx=i: trigger_clip(idx)

# Add the Kill Switch (Mod + Alt + K)
hotkeys[mod + "+<alt>+k"] = kill_script

print("MagicBoard is active.")
print("Hotkeys: " + friendly_mod + " + Option/Alt + [1-8]")
print("Kill Switch: " + friendly_mod + " + Option/Alt + K")

with pynput.keyboard.GlobalHotKeys(hotkeys) as h:
    h.join()