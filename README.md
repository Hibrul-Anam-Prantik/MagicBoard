# 🧙‍♂️ MagicBoard

**MagicBoard** is a high-efficiency, cross-platform clipboard manager. It allows you to map 8 different text files to global hotkeys, enabling "silent" copying of code snippets, SQL queries, or templates without a visible terminal window.

---

## 🛠️ Quick Start

### 1. Prerequisites

- **Python 3.x:** Download from [python.org](https://www.python.org/).
- **Crucial Step:** During installation, check the box **"Add Python to PATH"**.

### 2. Install Dependencies

Open your terminal (PowerShell on Windows or Terminal.app on Mac) and run:

```bash
pip install pynput pyperclip
```

If "pip" is not recognized, try: python -m pip install pynput pyperclip

## 📖 Step-by-Step Process

Follow these steps to use MagicBoard correctly:

### Step 1: Prepare Your Snippets

Open the folder and locate the files magic01.txt through magic08.txt. Open each one and paste the specific text or code you want to save. Save and close the files.
+4

### Step 2: Launch the Program

On Windows: Right-click launch.bat and select Run as Administrator. (This is necessary for the script to detect keys while you are in other apps).
+2

On macOS: Open Terminal, cd into the folder, and run sh launch.sh.

### Step 3: Trigger the Copy

Go to your target application (VS Code, SQL Workbench, Browser, etc.). Press the hotkey for the slot you want:

    Windows: Ctrl + Alt + [1-8]

    macOS: Command + Option + [1-8]

Example: Pressing Ctrl+Alt+1 loads the text from magic01.txt into your clipboard.
+2

### Step 4: Paste

Now simply press the standard paste shortcut `(Ctrl+V or Cmd+V)` to insert your text into the application.

### Step 5: Close/Kill the Program

When you are finished, use the "Kill Switch" to stop the background process:

#### Windows Kill Switch:

    Ctrl + Alt + K (Stops the program immediately).

#### macOS Kill Switch:

    Command + Option + K (Or run pkill -f Magician.py in Terminal).

---

## 🖥️ Platform Specifics

### Windows Users

The script launches silently via run_silent.vbs. You will not see a black window; the program runs entirely in the background.
+4

### macOS Users

macOS requires explicit permission for MagicBoard to "listen" to your keyboard:

Go to: System Settings > Privacy & Security > Accessibility.

Ensure Terminal (or Python) is toggled ON.
