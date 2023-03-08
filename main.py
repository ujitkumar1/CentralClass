import os
import glob
from bs4 import BeautifulSoup

# Get current working directory
cwd = os.getcwd()

# Use glob to find all .html files in cwd and its subdirectories
html_files = glob.glob(cwd + '/**/*.html', recursive=True)

# Loop through each HTML file
for file in html_files:
    with open(file, 'r',encoding="utf-8") as f:
        # Read the contents of the file
        contents = f.read()
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(contents, 'html.parser')
        
        # Find all <li> tags with the specified class and remove them
        for li in soup.find_all('li', {'class': 'bg-white border-all border-gray-light padding-xsmall radius-small margin-bottom-small medium-up-padding-horz-large medium-up-padding-vert-medium relative'}):
            li.decompose()
        
        # Write the modified contents back to the file
        with open(file, 'w',encoding="utf-8") as f2:
            f2.write(str(soup))
