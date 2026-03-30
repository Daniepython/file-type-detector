# File Type Spoofing Detection Tool

A Python-based cybersecurity tool that detects file type spoofing by analyzing file signatures (magic numbers) instead of relying on file extensions.

## Features
- Detects real file type using header analysis
- Flags mismatches between extension and actual type
- Supports multiple file formats (JPEG, PNG, EXE, ZIP, PDF, etc.)
- Folder scanning capability

## How it works
The tool reads the first few bytes of a file and compares them with a database of known magic numbers to identify the true file type.

## Usage
Run the script using:
python spoof_detector.py

## Example
Renaming a file like:
malware.exe → image.jpg

The tool will detect:
- Actual type: EXE
- Extension: JPG
- Result: Mismatch detected

## Limitations
- Some file types like .txt, .csv, and .html do not have fixed magic numbers and may appear as "unknown"
- Detection is based on known signatures only

## Author
Danie Immanuel
