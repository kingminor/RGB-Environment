import imghdr
from PIL import Image

file = open("Survival.png")
file_type = imghdr.what("Survival.png")
print(f"This file is a {file_type}")

filename = "Survival.png"
img=Image.open(filename)

length = img.size[0]
print(f"The length of the image is {length}")
height = img.size[1]
print(f"The height of the image is {height}")

l = input("Length:")
h = input("Height:")

colors = img.getpixel((l,h))
print(f"The selected pixel is {colors}")
