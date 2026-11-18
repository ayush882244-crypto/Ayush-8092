"""Run the three image examples in order. Turtle is run separately because it opens a window."""
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
SCRIPTS = ["v0_1_pillow.py", "v0_2_qrcode.py", "v0_3_combined.py"]


def main():
    for script in SCRIPTS:
        print(f"\n--- running {script} ---", flush=True)
        result = subprocess.run([sys.executable, str(PROJECT_DIR / script)], cwd=PROJECT_DIR)
        if result.returncode != 0:
            raise SystemExit(f"{script} failed with exit code {result.returncode}")
    print("\nall image examples completed successfully")
    print("run homework_turtle.py separately to open the turtle drawing window")


if __name__ == "__main__":
    main()
