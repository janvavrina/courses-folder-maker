# Folder Creator Script

This Python script allows you to create multiple folders from a comma-separated list of folder names. 
For each folder, it will automatically create two subfolders: `cviceni` and `prednasky`. You can change this in the code.

## Features
- Accepts a list of folder names as a single command-line argument.
- Creates the specified folders if they don't already exist.
- Inside each folder, creates two subfolders: `cviceni` and `prednasky`.
- Skips creating folders or subfolders if they already exist.

## Prerequisites
- Python 3.x installed on your system.

## Usage

### Step 1: Download the Script
Save the provided script as `create_folders.py` on your local machine preferably into the folder where you want the folders to be created.

### Step 2: Open Terminal
Navigate to the directory where the `create_folders.py` script is saved.

### Step 3: Run the Script
Use the following command to run the script. Replace the example folder names with your own:

```bash
python create_folders.py "folder1, folder2, folder3"
```

### Example

```bash
python create_folders.py "Course1,Course2,Course3"
```

This will create the following folder structure:
```
Course1/
    ├── cviceni/
    └── prednasky/
Course2/
    ├── cviceni/
    └── prednasky/
Course3/
    ├── cviceni/
    └── prednasky/
```

### Step 4: Handling Existing Folders
- If a folder or subfolder already exists, the script will skip creating it and will inform you in the output.

## Error Handling
If you do not provide the folder names correctly, you will see the following usage instruction:

```
Usage: python create_folders.py 'folder1,folder2,folder3'
```
