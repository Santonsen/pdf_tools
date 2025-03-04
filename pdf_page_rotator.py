#!/usr/bin/env python3

import PyPDF4 as PyPDF2
import sys

input_pdf = sys.argv[1]

base_name, suffix_name = input_pdf.rsplit('_',1)
suffix_name = suffix_name.split('.')[0]

output_pdf_name = '_'.join([base_name,suffix_name,'rotated.pdf'])


# read the orignal files
pdf_object = open(input_pdf, 'rb')

# create a pdf Reader object for each
pdf_reader = PyPDF2.PdfFileReader(pdf_object)


# create a new empty pdf object
pdf_writer = PyPDF2.PdfFileWriter()


for page in range(pdf_reader.numPages):
    # every other page rotate 180
    page_obj = pdf_reader.getPage(page)
    if page % 2:
    
        page_obj.rotateClockwise(180)

    pdf_writer.addPage(page_obj)

    
# write the pages to a new file
new_file = open(output_pdf_name, 'wb')
pdf_writer.write(new_file)


# close everything back up

pdf_object.close()

new_file.close()
