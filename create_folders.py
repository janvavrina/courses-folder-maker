import os
import sys

def create_folders(folder_names):
    # Split the comma-separated folder names
    folders = folder_names.split(',')

    # Iterate over each folder name
    for folder in folders:
        folder = folder.strip()  # Remove any extra whitespace
        if not folder:
            continue

        # Create the main folder
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        
        # Create subfolders 'cviceni' and 'prednasky'
        subfolders = ['cviceni', 'prednasky']
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"  Created subfolder: {subfolder_path}")
            else:
                print(f"  Subfolder {subfolder_path} already exists.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_folders.py 'folder1,folder2,folder3'")
    else:
        folder_names = sys.argv[1]
        create_folders(folder_names)
