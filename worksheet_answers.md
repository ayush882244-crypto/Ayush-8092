# worksheet 13b

name ayush raj

roll number 8092

campus not provided

## where did your first library land

run `python3 -m pip show pillow` to see the install location on your computer

## pick two

my two libraries are pillow and qrcode

why those two

i wanted to make an image and a qr code and then combine them

## set up the repository

repository name Ayush-8092

repository url https://github.com/ayush882244-crypto/Ayush-8092

## v0 1 your first library

library pillow

what is it for

pillow is used to open create edit and save images in python

docs

https://pillow.readthedocs.io/

first code block idea

```python
from PIL import Image
image = Image.new("RGB", (200, 100), "white")
image.save("first_image.png")
```

did it run

run the program with `python3 v0_1_pillow.py` and record the result after checking it on your computer

what did you get

the program is written to save a white image with the text hello ayush as pillow_output.png

before you ask

i wanted to create a simple image with my name on it

prompt used

write a beginner python program using pillow to create a white image and add the text hello ayush then save it as pillow_output.png explain each line

did the code run first time

record yes or no after running it

one line to understand

ImageDraw.Draw(image) creates a drawing object that lets me add text and shapes to the image

break it and check it

change the output path to a folder that does not exist then run it and write down the exact error shown in your terminal

## v0 2 your second library

library qrcode

what is it for

qrcode creates qr code images from text or links

docs

https://github.com/lincolnloop/python-qrcode

first code block

```python
import qrcode
image = qrcode.make("hello")
image.save("hello.png")
```

did it run

run the program with `python3 v0_2_qrcode.py` and record the result after checking it on your computer

what did you get

the program is written to save a qr code containing Ayush-8092 as qrcode_output.png

before you ask

i wanted to make a qr code containing my project name

prompt used

write a simple python program using qrcode to create a qr code for Ayush-8092 and save it as qrcode_output.png

one line to understand

qrcode.make creates a qr code image from the text i provide

break it and check it

remove the text argument from qrcode.make then run it and write down the exact error shown in your terminal

## v0 3 make them talk to each other

what will yours do

it will create a qr code with qrcode and use pillow to add a caption below it

what will the output look like if it works

a square qr code with the words project by ayush raj written below it

prompt used

combine qrcode and pillow in a beginner python program create a qr code for Ayush-8092 add a caption below it and save the final image as combined_output.png explain the code simply

how many times did you go back and forth

fill this in after testing and improving the program

what did you change about how you were asking

fill this in after testing and improving the program

something ai got wrong

check the suggested function names and arguments against the official documentation before writing a real example here

how did you find out it was wrong

compare the code with the official documentation and test the program

does it match what you predicted

check the generated image and record yes or no

## before you go

which was fastest

ai can be fastest for getting a code example

which was most reliable

official documentation is the source to check

were they the same

not always

## five steps from memory

1 find what the library is used for
2 read the quickstart and find the first example
3 run the smallest working example
4 change one thing and check the result
5 break it on purpose and read the error

## homework

library turtle

what is it for

turtle draws simple shapes using python commands and comes with python

what i built

a square with the project name written in the drawing window

run

```bash
python3 homework_turtle.py
```

after running it add the exact result and one thing that broke to your learning log
