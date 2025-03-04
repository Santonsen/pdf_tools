#!/usr/bin/env python3

import PyPDF2
import sys

input_pdf = sys.argv[1]

base_name, suffix_name = input_pdf.rsplit('_',1)
suffix_name = suffix_name.split('.')[0]

output_pdf_name = '_'.join([base_name,suffix_name,'reordered.pdf'])


# read the orignal files
pdf_object= open(input_pdf, 'rb')

# create a pdf Reader object for each
pdf_reader = PyPDF2.PdfFileReader(pdf_object)


# create a new empty pdf object
pdf_writer = PyPDF2.PdfFileWriter()

reordered_pages = []

for page in range(0,pdf_reader.numPages,2):
    # reorders the pages

    page_obj_1 = pdf_reader.getPage(page)
    page_obj_2 = pdf_reader.getPage(page+1)

    reordered_pages.insert(0, page_obj_1)
    reordered_pages.append(page_obj_2)

for reordered_page in reordered_pages:

    pdf_writer.addPage(reordered_page)
    
# write the pages to a new file
new_file = open(output_pdf_name, 'wb')
pdf_writer.write(new_file)


# close everything back up

pdf_object.close()

new_file.close()
