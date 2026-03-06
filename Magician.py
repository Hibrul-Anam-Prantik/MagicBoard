import pynput
from pynput.keyboard import Controller, Key
import os
import sys
import time

# keyboard controller init
keyboard = Controller()

# the text files should be in the same directory as this script
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
            CLIPS[index] = f"Error: {filename} not found."

def trigger_clip(index):
    """Types text directly into the active window, bypassing the clipboard"""
    content = CLIPS.get(index, "")
    if not content.startswith("Error:"):
        if sys.platform == 'darwin':
            keyboard.release(Key.cmd)
            keyboard.release(Key.alt)
        else:
            keyboard.release(Key.ctrl)
            keyboard.release(Key.alt)
        
        time.sleep(0.1)
        
        # pasting the text directly!
        keyboard.type(content)
        print(f"Injected clip {index} directly.")

def kill_script():
    """Stops the background process safely"""
    print("MagicBoard shutting down...")
    os._exit(0)

load_clips()

# setting up Modifiers: 'cmd' for Mac, 'ctrl' for Windows
mod = '<cmd>' if sys.platform == 'darwin' else '<ctrl>'
friendly_mod = "Command" if sys.platform == 'darwin' else "Ctrl"

# building hotkey dictionary
hotkeys = {f'{mod}+<alt>+{i}': lambda i=i: trigger_clip(i) for i in CLIPS.keys()}
hotkeys[f'{mod}+<alt>+k'] = kill_script

print("MagicBoard is active (Direct Injection Mode).")
print(f"Hotkeys: {friendly_mod} + Option/Alt + [1-8]")
print(f"Kill Switch: {friendly_mod} + Option/Alt + K")

with pynput.keyboard.GlobalHotKeys(hotkeys) as h:
    h.join()


Don't reply to this