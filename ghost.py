import keyboard
import pyperclip
import time
import sys
import os

# Define the file paths for the 8 clips
CLIP_FILES = {
    "1": "clip_1.txt",
    "2": "clip_2.txt",
    "3": "clip_3.txt",
    "4": "clip_4.txt",
    "5": "clip_5.txt",
    "6": "clip_6.txt",
    "7": "clip_7.txt",
    "8": "clip_8.txt",
}

CLIPS = {}

def load_clips():
    """Reads the content from the text files into the CLIPS dictionary."""
    print("Loading clips from external files...")
    for index, filename in CLIP_FILES.items():
        try:
            # Use 'with open' for safe file handling
            with open(filename, 'r', encoding='utf-8') as f:
                # Store the entire file content, stripping leading/trailing whitespace
                CLIPS[index] = f.read().strip()
            print(f"  Successfully loaded clip {index} from {filename}")
        except FileNotFoundError:
            print(f"  ERROR: File not found for clip {index}: {filename}")
            CLIPS[index] = f"ERROR: Content file not found ({filename})"
        except Exception as e:
            print(f"  ERROR loading clip {index} from {filename}: {e}")
            CLIPS[index] = f"ERROR: Could not read content from file ({filename})"

# Load the clips when the script starts
load_clips()

def make_handler(index):
    """Creates a function that copies the content corresponding to the index."""
    def handler():
        try:
            content = CLIPS.get(index, "")
            if content.startswith("ERROR"):
                 # If content starts with ERROR, print a warning for debugging 
                 # (not visible when silent, but useful for testing)
                print(content)
                return
                
            pyperclip.copy(content)
            # This print statement won't be visible when running silently via VBS,
            # but is useful if you run the script directly for testing.
            print(f"Copied clip {index} to clipboard. Hotkey: ctrl+alt+{index}")
        except Exception as e:
            # Added basic error handling
            print(f"Error copying clip {index}: {e}")
    return handler

print("Clipboard Hotkey Service is starting. Press CTRL+C to stop.")

# Map hotkeys (shift+ctrl+alt+1 to shift+ctrl+alt+8) to the clipboard content.
for i in CLIPS.keys():
    # Hotkeys are defined as "shift+ctrl+alt+1", "shift+ctrl+alt+2", etc.
    hotkey_combo = f"ctrl+alt+{i}"
    keyboard.add_hotkey(hotkey_combo, make_handler(i))
    print(f"Registered hotkey: {hotkey_combo}")

try:
    # Keeps the script running and listening for hotkeys
    keyboard.wait()
except KeyboardInterrupt:
    print("Service stopped by user.")
    sys.exit(0)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)