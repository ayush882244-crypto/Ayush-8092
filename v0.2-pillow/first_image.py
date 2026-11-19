from PIL import Image

image = Image.new("RGB", (400, 300), "blue")
image.save("first_image.png")

print("image created successfully")
