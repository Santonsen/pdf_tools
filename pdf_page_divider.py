#!/usr/bin/env python3

import PyPDF4 as PyPDF2
import sys

input_pdf = sys.argv[1]

base_name, suffix_name = input_pdf.rsplit('_',1)
suffix_name = suffix_name.split('.')[0]

output_pdf_name = '_'.join([base_name,suffix_name,'divided.pdf'])


# read the orignal files
pdf_object= open(input_pdf, 'rb')

# create a pdf Reader object for each
pdf_reader = PyPDF2.PdfFileReader(pdf_object)
pdf_reader_2 = PyPDF2.PdfFileReader(pdf_object)


# create a new empty pdf object
pdf_writer = PyPDF2.PdfFileWriter()


for page in range(pdf_reader.numPages):
    # every pages gets cut in two vertically
    # creates two pages

    page_obj= pdf_reader.getPage(page)
    page_width_from = page_obj.mediaBox.getUpperLeft_x()
    page_width_to = page_obj.mediaBox.getUpperRight_x()
    page_width_half = page_width_to / 2

    # trim first half
    page_obj.mediaBox.lowerLeft = (page_obj.mediaBox.getLowerLeft_x(), page_obj.mediaBox.getLowerLeft_y())
    page_obj.mediaBox.upperRight = (page_width_half, page_obj.mediaBox.getUpperRight_y())

    page_obj_2 = pdf_reader_2.getPage(page)
    page_width_from = page_obj_2.mediaBox.getUpperLeft_x()
    page_width_to = page_obj_2.mediaBox.getUpperRight_x()
    page_width_half = page_width_to / 2

    # trim second half 
    page_obj_2.mediaBox.lowerLeft = (page_width_half, page_obj_2.mediaBox.getLowerLeft_y())
    page_obj_2.mediaBox.upperRight = (page_obj_2.mediaBox.getUpperRight_x(), page_obj_2.mediaBox.getUpperRight_y())

    pdf_writer.addPage(page_obj)
    pdf_writer.addPage(page_obj_2)

    
# write the pages to a new file
new_file = open(output_pdf_name, 'wb')
pdf_writer.write(new_file)


# close everything back up

pdf_object.close()

new_file.close()
