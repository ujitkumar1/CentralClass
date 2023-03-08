import os
import re

# define the regex pattern to match the string we want to replace
pattern = re.compile(r'\|\|\|UNTRANSLATED_CONTENT_(START|END)\|\|\|')

# walk through the directory tree and find all .html files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            # open the file and read its contents
            filepath = os.path.join(root, file)
            with open(filepath, "r",encoding="utf-8") as f:
                contents = f.read()
            
            # replace the pattern with an empty string
            contents = re.sub(pattern, "", contents)
            
            # overwrite the file with the modified contents
            with open(filepath, "w",encoding="utf-8") as f:
                f.write(contents)
