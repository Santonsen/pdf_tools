#!/usr/bin/env python3

# Use this to split into parts

import PyPDF4 as PyPDF2
from itertools import chain
import sys

input_pdf = sys.argv[1]

ranges = [0,16,28,35,45,48,55,60]

partnames = {'cornets' : range(ranges[0], ranges[1]),
             'horns' : range(ranges[1], ranges[2]),
             'euphbari' : chain(range(ranges[2], ranges[3]), range(ranges[4], ranges[5])),
             #'euphbari' : range(22, 28),
             'trombones' : range(ranges[3],ranges[4]),
             'tubas' : range(ranges[5], ranges[6]),
             'percussion' : range(ranges[6], ranges[7])}


def new_pdf_from_range(input_pdf_name, output_pdf_name, page_range):
    # read the original file
    pdf_file_object = open(input_pdf_name, 'rb')

    # create a pdf Reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)

    # create a new empty pdf
    pdf_writer = PyPDF2.PdfFileWriter()

    for page in page_range:
        page_obj = pdf_reader.getPage(page)

        # add the page object to pdf writer
        pdf_writer.addPage(page_obj)

    # new pdf file object
    new_file = open(output_pdf_name, 'wb')

    # writing pages to new file
    pdf_writer.write(new_file)

    # closing the original pdf file object
    pdf_file_object.close()

    # closing the new pdf file object
    new_file.close()
    

for part in partnames:

    output_pdf = input_pdf.replace('parts',(part))
    
    new_pdf_from_range(input_pdf, output_pdf, partnames[part])
