# ayush 8092

beginner python examples for worksheet 13b

## what it does

this project creates an image with pillow, creates a qr code with qrcode, combines the qr code with a caption, and draws a square with turtle

the qr code contains the link to this github repository

## requirements

- python 3.9 or newer
- pillow
- qrcode with pillow support
- turtle is included with the standard python installation

## setup on mac

open terminal and move into the folder where you downloaded this repository

```bash
cd Ayush-8092
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## run the image examples

run all three image programs with one command

```bash
python run_all.py
```

you can also run each version separately

```bash
python v0_1_pillow.py
python v0_2_qrcode.py
python v0_3_combined.py
```

the programs save `pillow_output.png`, `qrcode_output.png`, and `combined_output.png` in the project folder even when you start them from another directory

## run the turtle homework

```bash
python homework_turtle.py
```

this opens a drawing window, draws a square, and writes the project name below it. turtle needs a desktop display, so it may not work in a headless terminal or remote server

## output files

- `pillow_output.png` a white image with hello ayush
- `qrcode_output.png` a qr code linking to this repository
- `combined_output.png` the qr code with a caption underneath
- turtle draws directly in its own window

## limitations

the examples are intentionally small and do not have a graphical menu or advanced error handling. the turtle drawing is interactive only through its window

## deactivate the virtual environment

```bash
deactivate
```
