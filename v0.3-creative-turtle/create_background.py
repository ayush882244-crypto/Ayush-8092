from pathlib import Path
from PIL import Image

folder = Path(__file__).resolve().parent
background = Image.new("RGB", (900, 650), "#080820")
background.save(folder / "background.gif", "GIF")

print("background created successfully")
