import qrcode

data = input('Enter the text or URL: ').strip()

filename = input('Enter the filename: ').strip()

qr = qrcode.QRCode(box_size=10, border=10)

qr_image = qr.make_image(back_color='white', fill_color='black')

qr_image.save(filename + '.png')