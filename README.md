# CIS_442-Masquerade-Project
This program is a CIS 442 project at The University of Massachusetts Dartmouth

## Description
This program will list all the masquerade files within a given folder. The program uses the python-magic library to read file signatures from the mime files, then compares those results with the files extension. When the read extension doesn't match the files signature, the program returns the masquerade file's name.

## Install
### Python
Make sure you have the latest version of python installed <br />
Download here: https://www.python.org/downloads/ <br />

### Python-Magic
Install Python-Magic <br />
```python
pip install python-magic
```
### Libmagic
Install Python-Libmagic
```python
pip isntall python-libmagic
```
### Copy Repository
Clone repository to your local machine <br />
```python
git clone https://github.com/Philp5/CIS_442-Masquerade-Project.git
```

## Usage
1. Run the script
```python
Python fileSigCheck.py
```
2. You will be prompted to enter a folder path
```python
'/enter/your/folder/path'
```
This will print out any files within the given directory that has a signature different from the extension type

## How it Works
- The program uses os.walk to scan through every folder and file in the given directory
- os.path is used to read a file and get its full path
- magic.Magic() is used to create a mime variable which can be utilized to read the signature from the file path
- os.path is used again to split the file extension from the file name, then the leading period is removed
- The program compares the extension witht he beginning of the file signature and prints out the file name if they don't match



