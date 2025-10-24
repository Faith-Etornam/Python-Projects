import pypdf

with open('dummy.pdf', 'rb') as my_pdf:
    reader = pypdf.PdfReader(my_pdf)
    rotated_pdf = reader.pages[0].rotate(90)
    writer = pypdf.PdfWriter()
    writer.add_page(rotated_pdf)
    with open('new.pdf', 'wb') as new_file:
        writer.write(new_file)

