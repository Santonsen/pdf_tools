#!/usr/bin/env python3

# Use this to split into parts

import pypdf
from itertools import chain
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a complete set of score and parts.")
    parser.add_argument("input_pdf", type=str, help="Path to the input PDF file.")
    parser.add_argument("ranges", type=int, nargs='+', help="Specify sections. The pdf needs to be in score order.\n0 0 16 28 35 45 48 55 60\nThis is an example where there is no score, then the order is\n cornets horns bari trombones euph tuba perc")
    return parser.parse_args()

def new_pdf_from_range(input_pdf_name, output_pdf_name, page_range):
    # read the original file
    pdf_file_object = open(input_pdf_name, 'rb')

    # create a pdf Reader object
    pdf_reader = pypdf.PdfReader(pdf_file_object)

    # create a new empty pdf
    pdf_writer = pypdf.PdfWriter()

    for page in page_range:
        page_obj = pdf_reader.get_page(page)

        # add the page object to pdf writer
        pdf_writer.add_page(page_obj)

    # new pdf file object
    new_file = open(output_pdf_name, 'wb')

    # writing pages to new file
    pdf_writer.write(new_file)

    # closing the original pdf file object
    pdf_file_object.close()

    # closing the new pdf file object
    new_file.close()

def main():
    args = parse_arguments()

    print(f"Processingt PDF: {args.input_pdf}")
    print(f"Using section ranges: {args.ranges}")

    partnames = {
        'score' : range(args.ranges[0], args.ranges[1]),
        'cornets' : range(args.ranges[1], args.ranges[2]),
        'horns' : range(args.ranges[2], args.ranges[3]),
        'euphbari' : chain(range(args.ranges[3], args.ranges[4]), range(args.ranges[5], args.ranges[6])),
        'trombones' : range(args.ranges[4],args.ranges[5]),
        'tubas' : range(args.ranges[6], args.ranges[7]),
        'percussion' : range(args.ranges[7], args.ranges[8])
    }

    print(f"Using partnames: {partnames}")


    for part in partnames:
        output_pdf = args.input_pdf.replace('_parts_', f"_{part}_")
        print(output_pdf)
        new_pdf_from_range(args.input_pdf, output_pdf, partnames[part])

if __name__ == "__main__":
    main()

