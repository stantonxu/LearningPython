from PIL import Image

img1 = Image.open("sx1.JPG")
img2 = Image.open("sx2.JPG")
area = (10, 10, 1900, 1900)
cropped_img1 = img1.crop(area)
cropped_img2 = img2.crop(area)

r1, g1, b1 = cropped_img1.split()
r2, g2, b2 = cropped_img2.split()

new_img = Image.merge("RGB", (r1, g2, b2))
new_img.show()