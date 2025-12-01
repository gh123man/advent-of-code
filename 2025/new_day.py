#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Find all numbered directories
numbered_dirs = []
for item in script_dir.iterdir():
    if item.is_dir() and item.name.isdigit():
        numbered_dirs.append(int(item.name))

# Find the next number
next_num = max(numbered_dirs) + 1 if numbered_dirs else 1

# Create the new directory
new_dir = script_dir / str(next_num)
new_dir.mkdir(exist_ok=True)

# Template file path
template_file = script_dir / "template" / "main.py"

# Copy template to main.py
if template_file.exists():
    shutil.copy(template_file, new_dir / "main.py")
    print(f"Created {new_dir / 'main.py'}")
else:
    print(f"Warning: Template file not found at {template_file}")

# Create empty input.txt
input_file = new_dir / "input.txt"
input_file.touch()
print(f"Created {input_file}")

print(f"\nCreated new day folder: {new_dir}")

