from PIL import Image, ImageDraw

# create a white image
image = Image.new("RGB", (500, 250), "white")

# prepare to draw on the image
draw = ImageDraw.Draw(image)

# write a short message
draw.text((30, 100), "hello ayush", fill="black")

# save the image
image.save("pillow_output.png")

print("saved pillow_output.png")
