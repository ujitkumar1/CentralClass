import os
import shutil

# Define the function to rename the .html files
def rename_html_files(path):
    # Loop through all the subdirectories in the given path
    for root, dirs, files in os.walk(path):
        # Loop through all the files in each subdirectory
        for file in files:
            # Check if the file is a .html file
            if file.endswith('.html'):
                # Construct the new file name as "index.html"
                new_file_name = os.path.join(root, 'index.html')
                # Rename the file to "index.html"
                shutil.move(os.path.join(root, file), new_file_name)

# Call the function with the current working directory as the argument
rename_html_files(os.getcwd())
