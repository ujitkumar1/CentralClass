import os
from bs4 import BeautifulSoup

# walk through the directory tree and find all .html files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            # open the file and read its contents
            filepath = os.path.join(root, file)
            with open(filepath, "r",encoding="utf-8") as f:
                contents = f.read()

            # parse the HTML using BeautifulSoup
            soup = BeautifulSoup(contents, "html.parser")

            # find all img tags and modify their attributes
            for img in soup.find_all("img"):
                if img.has_attr("data-src"):
                    if img.has_attr("src"):
                        del img["src"]
                    img["src"] = img["data-src"]
                    del img["data-src"]

            # write the modified contents back to the file
            with open(filepath, "w",encoding="utf-8") as f:
                f.write(str(soup))
