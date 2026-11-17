import qrcode

# make a qr code containing the project name
image = qrcode.make("Ayush-8092")

# save the qr code image
image.save("qrcode_output.png")

print("saved qrcode_output.png")
