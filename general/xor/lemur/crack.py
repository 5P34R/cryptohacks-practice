from PIL import Image, ImageChops

im1 = Image.open('lemur.png')
im2 = Image.open('flag.png')

im3 = ImageChops.add(ImageChops.subtract(im1, im1), ImageChops.subtract(im1, im2))
im3.save("img.png")
# with open("res.png", "wb") as f:
#     f.write(res)

