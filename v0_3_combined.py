import qrcode
from PIL import Image, ImageDraw

# create a qr code
qr_image = qrcode.make("Ayush-8092").convert("RGB")

# make a larger white image for the qr code and caption
canvas = Image.new("RGB", (qr_image.width, qr_image.height + 70), "white")
canvas.paste(qr_image, (0, 0))

# add a caption below the qr code
draw = ImageDraw.Draw(canvas)
draw.text((10, qr_image.height + 25), "project by ayush raj", fill="black")

# save the combined image
canvas.save("combined_output.png")

print("saved combined_output.png")
