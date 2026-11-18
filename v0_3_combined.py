from pathlib import Path
import qrcode
from PIL import Image, ImageDraw, ImageFont

REPOSITORY_URL = "https://github.com/ayush882244-crypto/Ayush-8092"


def main():
    output_path = Path(__file__).resolve().parent / "combined_output.png"
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(REPOSITORY_URL)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    padding = 24
    caption = "project by ayush raj"
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except OSError:
        font = ImageFont.load_default()

    measure = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    left, top, right, bottom = measure.textbbox((0, 0), caption, font=font)
    caption_width = right - left
    caption_height = bottom - top
    canvas = Image.new(
        "RGB",
        (max(qr_image.width, caption_width + 2 * padding), qr_image.height + caption_height + 3 * padding),
        "white",
    )
    qr_x = (canvas.width - qr_image.width) // 2
    canvas.paste(qr_image, (qr_x, padding))
    draw = ImageDraw.Draw(canvas)
    text_x = (canvas.width - caption_width) // 2
    text_y = qr_image.height + 2 * padding
    draw.text((text_x, text_y), caption, fill="black", font=font)
    canvas.save(output_path)
    print(f"success: combined image saved to {output_path}")
    print(f"qr code links to {REPOSITORY_URL}")


if __name__ == "__main__":
    main()
