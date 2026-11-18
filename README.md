# ayush 8092

beginner python examples for worksheet 13b

## run automatically on github

github actions runs the three image programs automatically whenever code is pushed to the main branch or a pull request is opened. you can also start a run manually

1. open the repository on github
2. select the actions tab
3. choose run python examples
4. select run workflow

when the run finishes, open the run and download the generated images from the artifacts section

## what it does

this project creates an image with pillow, creates a qr code with qrcode, combines the qr code with a caption, and draws a square with turtle

the qr code contains the link to this github repository

## requirements

- python 3.9 or newer
- pillow
- qrcode with pillow support
- turtle is included with the standard python installation

## run locally on mac

```bash
git clone https://github.com/ayush882244-crypto/Ayush-8092.git
cd Ayush-8092
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_all.py
```

the programs save `pillow_output.png`, `qrcode_output.png`, and `combined_output.png` in the project folder

## run turtle locally

```bash
python homework_turtle.py
```

this opens a drawing window, draws a square, and writes the project name below it. turtle needs a desktop display, so it is not run by the github actions workflow because github's runner has no graphical desktop

## output files

- `pillow_output.png` a white image with hello ayush
- `qrcode_output.png` a qr code linking to this repository
- `combined_output.png` the qr code with a caption underneath
- turtle draws directly in its own window

## limitations

the examples are intentionally small and do not have a graphical menu or advanced error handling
