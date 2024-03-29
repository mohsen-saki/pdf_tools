"""
Grab all PDF files in root directory and
merge them into  a single PDF file.
If thier order maters, make sure to rename them to keep prefered order

Usage: $ python merger.py
return: creats a pdf file named "merged.pdf"
"""


from PyPDF2 import PdfFileMerger
import glob
from pathlib import Path
import sys
sys.path.append("..")

def get_merged_pdf():
    """
    merge separate PDF files as a single file
    :return: creat a pdf file at the script current address
    """
    files = [file for file in glob.glob("*.pdf")]
    if len(files) == 0:
        print("No PDF file(s) found in the current address!")
    else:
        merger = PdfFileMerger()
        for file in files:
            merger.append(file)
        with open ("merged.pdf", "wb") as outfile:
            merger.write(outfile)


get_merged_pdf()
print("Succesfully merged :)")
