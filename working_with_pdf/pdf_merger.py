import pypdf


template = pypdf.PdfReader(open('merged.pdf', 'rb'))

watermark = pypdf.PdfReader(open('wtr.pdf', 'rb'))

output = pypdf.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[0]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked.pdf', 'wb') as new_pdf_file:
        output.write(new_pdf_file)




# inputs = sys.argv[1:]

# def pdf_merger(pdf_list):
#     merger = pypdf.PdfWriter()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('merged.pdf')
#     merger.close()

# pdf_merger(inputs)
