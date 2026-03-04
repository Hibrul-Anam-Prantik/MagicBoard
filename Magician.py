import keyboard
import pyperclip
import time
import sys
import os

CLIP_FILES = {
    "1": "magic01.txt",
    "2": "magic02.txt",
    "3": "magic03.txt",
    "4": "magic04.txt",
    "5": "magic05.txt",
    "6": "magic06.txt",
    "7": "magic07.txt",
    "8": "magic08.txt",
}

CLIPS = {}

def load_clips():
    """Reads the content from the text files into the CLIPS dictionary."""
    print("Loading clips from external files...")
    for index, filename in CLIP_FILES.items():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                CLIPS[index] = f.read().strip()
            print(f"  Successfully loaded clip {index} from {filename}")
        except FileNotFoundError:
            print(f"  ERROR: File not found for clip {index}: {filename}")
            CLIPS[index] = f"ERROR: Content file not found ({filename})"
        except Exception as e:
            print(f"  ERROR loading clip {index} from {filename}: {e}")
            CLIPS[index] = f"ERROR: Could not read content from file ({filename})"

load_clips()

def make_handler(index):
    def handler():
        try:
            content = CLIPS.get(index, "")
            if content.startswith("ERROR"):
                print(content)
                return
                
            pyperclip.copy(content)
            print(f"Copied clip {index} to clipboard. Hotkey: ctrl+alt+{index}")
        except Exception as e:
            print(f"Error copying clip {index}: {e}")
    return handler

print("Clipboard Hotkey Service is starting. Press CTRL+C to stop.")

for i in CLIPS.keys():
    hotkey_combo = f"ctrl+alt+{i}"
    keyboard.add_hotkey(hotkey_combo, make_handler(i))
    print(f"Registered hotkey: {hotkey_combo}")

try:
    keyboard.wait()
except KeyboardInterrupt:
    print("Service stopped by user.")
    sys.exit(0)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)