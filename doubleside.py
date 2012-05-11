#!/usr/bin/env python

import sys, os, glob
from pyPdf import PdfFileWriter, PdfFileReader

if len(sys.argv) != 3:
  print 'Usage: python doublespace.py ./my_folder_of_pdfs/ output.pdf'
  exit()

input_folder = sys.argv[1]
output_file  = sys.argv[2]
work_directory = os.path.abspath(input_folder)

# python's default recursion limit is 1000
# so pdf files over 1000 pages crashes the program with a
# recusion limit error. Lets set it higher.
sys.setrecursionlimit(2000)

# determine if number is odd or not
def is_odd(num):
    return (num & 1)

# we'll need a blank file and an output object to push data into
blank_page  = PdfFileReader(file("blank.pdf", "rb")).getPage(0)
output      = PdfFileWriter()

# iterate over all .pdf files in directory
for filename in glob.glob(os.path.join(work_directory, '*.pdf')):
    pdf = PdfFileReader(file(filename, "rb"))
    print "working on file %s \n" % filename
    pdf_page_count = pdf.getNumPages()

    # iterate over pdf and push each page into a new file
    for i in range(0, pdf_page_count):
        page = pdf.getPage(i)
        output.addPage(page)

    # if there are an odd number of pages in the pdf, add a blank page
    if is_odd(pdf_page_count):
        #add blank page at end
        output.addPage(blank_page)


outputStream = file(output_file, "wb")
output.write(outputStream)
outputStream.close()