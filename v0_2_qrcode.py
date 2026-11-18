from pathlib import Path
import qrcode

REPOSITORY_URL = "https://github.com/ayush882244-crypto/Ayush-8092"


def main():
    output_path = Path(__file__).resolve().parent / "qrcode_output.png"
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(REPOSITORY_URL)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(output_path)
    print(f"success: qr code saved to {output_path}")
    print(f"it links to {REPOSITORY_URL}")


if __name__ == "__main__":
    main()
