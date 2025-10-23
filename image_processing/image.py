from PIL import Image, ImageFilter

img = Image.open('./pokemon_images/pikachu.webp')

filtered_image = img.convert('L')

resized = filtered_image.resize((300,300))

resized.save('grey.png', 'png')


