# worksheet 13b

name ayush raj

roll number 8092

## v0.1 turtle

**what is it for**

turtle is used to draw shapes and patterns with python commands

**documentation**

https://docs.python.org/3/library/turtle.html

**smallest working program**

```python
import turtle

turtle.forward(100)
turtle.done()
```

**my experiment**

i used loops and different colours to draw repeated squares

**one thing i learned**

pen.forward(100) moves the turtle forward by 100 units

**testing**

run the program on a computer with a graphical desktop and note the actual output

## v0.2 pillow

**what is it for**

pillow is used to create edit and save images

**documentation**

https://pillow.readthedocs.io/en/stable/

**smallest working program**

```python
from PIL import Image

image = Image.new("RGB", (400, 300), "blue")
image.save("first_image.png")
```

**my experiment**

i changed the background colour and saved the image

**one thing i learned**

Image.new creates a new image with the size and colour i choose

## v0.3 creative turtle

**what did i want to build**

i wanted to make a colourful geometric sea turtle

**prompt used**

help me combine pillow and turtle to make a simple colourful sea turtle and explain the code in beginner friendly words

**how it works**

pillow creates the background image and turtle draws the shell head eyes flippers and tail

**what i learned**

two different python libraries can work together in one project

**testing**

run the program on a computer with a graphical desktop and check the drawing

## four information sources

- help command — useful for checking command options
- manual — useful for detailed information
- official documentation — reliable for checking library functions
- ai — useful for getting a quick explanation and example

**fastest**

ai is usually fastest for a first explanation

**most reliable**

official documentation is best for checking correct usage

**were they the same**

not always

## five steps for a new library

1 find what the library is used for
2 read the official documentation
3 run the smallest working example
4 change one thing and check the result
5 test an error and understand the message

## v0.4 homework — pyfiglet

**what is it for**

pyfiglet converts normal text into large ascii art banners

**installation**

```bash
python -m pip install pyfiglet
```

**python code**

```python
import pyfiglet

banner = pyfiglet.figlet_format("AYUSH", font="slant")
print(banner)
```

**my experiment**

i used my name ayush and printed it as a banner

**what i learned**

figlet_format converts normal text into ascii art
