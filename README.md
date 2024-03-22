# Duplicate File Remover

## Overview
This Python script helps to identify and remove duplicate files within a specified directory and its subdirectories. It calculates the hash of each file using the SHA-256 algorithm and compares them to find duplicates. If duplicates are found, the script removes them, keeping only one instance of each file.

## Prerequisites
- Python 3.x
- hashlib module (included in Python standard library)

## Usage
1. Make sure you have Python installed on your system.
2. Download the script (`nienteduplicati.py`) to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the following command:

    ```
    python3 nienteduplicati.py <directory_path>
    ```

    Replace `<directory_path>` with the path of the directory you want to scan for duplicate files.

6. The script will recursively search through the specified directory and its subdirectories, identifying and removing duplicate files.

## Important Note
- Exercise caution while using this script, as it permanently deletes files. Make sure to double-check the directory path before executing the script.
- Ensure you have appropriate permissions to delete files within the specified directory.
- I don't take any responsibility for the script. Use as you want.
