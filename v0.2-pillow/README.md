# v0.2 pillow

## what is pillow

pillow is a python library used to create edit open and save images

## documentation

https://pillow.readthedocs.io/en/stable/

## install

```bash
python -m pip install Pillow
```

## first program

```python
from PIL import Image

image = Image.new("RGB", (400, 300), "blue")
image.save("first_image.png")
```

## experiment

change the background colour from blue to another valid colour and run the program again

## what i learned

- how to create a new image
- how to choose image size and colour
- how to save an image as a png file
