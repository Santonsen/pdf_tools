#!/usr/bin/env python3

import PyPDF2
import sys

input_pdf_A = sys.argv[1]
input_pdf_B = sys.argv[2]



output_pdf_name = input_pdf_B.replace('_scoreB','_score')
print(output_pdf_name)


# read the orignal files
pdf_object_A = open(input_pdf_A, 'rb')

pdf_object_B = open(input_pdf_B, 'rb')

# create a pdf Reader object for each
pdf_reader_A = PyPDF2.PdfFileReader(pdf_object_A)

pdf_reader_B = PyPDF2.PdfFileReader(pdf_object_B)

# create a new empty pdf object
pdf_writer = PyPDF2.PdfFileWriter()

'''
# get every page of A then add it to the new pdf
for page in range(pdf_reader_A.numPages):
    page_obj = pdf_reader_A.getPage(page)
    pdf_writer.addPage(page_obj)

# get every page of B then add it to the new pdf
for page in range(pdf_reader_B.numPages):
    page_obj = pdf_reader_B.getPage(page)
    pdf_writer.addPage(page_obj)
'''
setA = range(11)
setB = range(10)

for i in range(11):
    page_obj_A = pdf_reader_A.getPage(i)
    pdf_writer.addPage(page_obj_A)

    n = ((i+1)*-1)
    if n >= -10:
        print(n)
        page_obj_B = pdf_reader_B.getPage(n)
        pdf_writer.addPage(page_obj_B)


    
# write the pages to a new file
new_file = open(output_pdf_name, 'wb')
pdf_writer.write(new_file)


# close everything back up

pdf_object_A.close()
pdf_object_B.close()
new_file.close()
