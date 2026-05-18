from pathlib import Path

from PIL import Image


def read_image(image_path: str) -> Image.Image:
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {path}")

    image = Image.open(path)
    print(f"Path: {path}")
    print(f"Mode: {image.mode}")
    print(f"Size: {image.size}")
    return image


if __name__ == "__main__":
    read_image("data/sample.png")
