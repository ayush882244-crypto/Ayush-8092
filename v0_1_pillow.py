from pathlib import Path
from PIL import Image, ImageDraw


def main():
    output_path = Path(__file__).resolve().parent / "pillow_output.png"
    image = Image.new("RGB", (600, 300), "white")
    draw = ImageDraw.Draw(image)
    draw.text((40, 120), "hello ayush", fill="black")
    image.save(output_path)
    print(f"success: image saved to {output_path}")


if __name__ == "__main__":
    main()
