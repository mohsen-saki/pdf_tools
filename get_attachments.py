"""
To extract attachments embeded in a PDF file
Usage: $ python get_attachment.py YOURFILE.PDF
return: save whatever attachments are embeded in pdf file

Thanks to: https://gist.github.com/kevinl95/29a9e18d474eb6e23372074deff2df38#file-extract_pdf_attachments-py
"""

import PyPDF2
from sys import argv

def get_attach(reader):
    """
    Retrieves the file attachments of the PDF as a dictionary of file names
    and the file data as a bytestring.
    :return: dictionary of filenames and bytestrings
    """

    catalog = reader.trailer["/Root"]
    file_names = catalog['/Names']['/EmbeddedFiles']['/Names']
    attachments = {}
    for f in file_names:
        if isinstance(f, str):
            name = f
            dataIndex = file_names.index(f) + 1
            fDict = file_names[dataIndex].getObject()
            fData = fDict['/EF']['/F'].getData()
            attachments[name] = fData

    return attachments


if len(argv) != 2:
    print("\nWRONG USAGE!")
    print("Try: $ python get_attachment.py YOURFILE.PDF\n")
else:
    handler = open(argv[1], 'rb')
    reader = PyPDF2.PdfFileReader(handler)
    dictionary = get_attach(reader)
    for fName, fData in dictionary.items():
        with open(fName, 'wb') as outfile:
            outfile.write(fData)
    print("Succesfully extracted :)")