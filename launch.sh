#!/bin/bash
cd "$(dirname "$0")"
chmod +x launch.sh
pip3 install pynput pyperclip --quiet
nohup python3 Magician.py > /dev/null 2>&1 &
echo "Magician started! Use Cmd+Option+[1-8]"