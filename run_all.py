"""run the examples that do not need a graphics window"""
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    "v0_1_pillow.py",
    "v0_2_qrcode.py",
    "v0_3_combined.py",
    "v0.2-pillow/first_image.py",
    "v0.4-pyfiglet/first_banner.py",
]


def main():
    for script in SCRIPTS:
        print(f"\n--- running {script} ---", flush=True)
        result = subprocess.run(
            [sys.executable, str(PROJECT_DIR / script)],
            cwd=PROJECT_DIR,
        )
        if result.returncode != 0:
            raise SystemExit(f"{script} failed with exit code {result.returncode}")

    print("\nall non-graphical examples completed successfully")
    print("run the turtle files separately on a computer with a desktop display")


if __name__ == "__main__":
    main()
