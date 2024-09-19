Time Sorted File Organiser
=====================================
About
--------
This script is designed to simplify file management by sorting files in a directory by their modified time and renaming them with a customizable prefix and serial number.
Features
------------
Sorts files by modified time in descending order
Renames files with a customizable prefix and serial number
Supports filtering by file extension
Written in Python for cross-platform compatibility
Installation
---------------
Step 1: Clone the Repository
```Bash
git clone https://github.com/maak47/time-sorted-file-organiser.git
```
Step 2: Navigate to the Repository Directory
```Bash
cd time-sorted-file-organiser
```
Step 3: Install Required Dependencies
```Bash
pip install -r requirements.txt
```
Note: No dependencies are required currently.

Thank you for clarifying.
So, the suffix parameter is used to filter files by their extension, not to rename the extension itself.
To make this clearer in the README, I'll update the documentation:
Usage
---------
Run the script with Python
```Bash
  python time_sorted_file_organiser.py /path/to/directory prefix extension
```
Replace:
/path/to/directory with the desired directory path
prefix with the desired file prefix
extension with the file extension to filter by (e.g., js, txt, etc.)
Note: The script will only rename files with the specified extension, leaving other files unchanged.
Example
----------- 
Rename JavaScript files in the /home/maak/spam directory with the prefix spam
```Bash
  python time_sorted_file_organiser.py /home/maak/spam spam js
```

Contributing
---------------
Contributions are welcome!
Fork the repository
Make changes and commit them
Create a pull request

Author
Maak47
--------
Thank you for using Time Sorted File Organiser!
