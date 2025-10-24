import pypdf
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')
    merger.close()

pdf_merger(inputs)
