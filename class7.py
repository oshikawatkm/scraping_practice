from PIL import Image
img = Image.open('default_icon.jpg')
img.size
img = img.resize((300, 300))
img.save('sample.jpg')