# Image Encryption Tool

This is a simple Python-based tool for encrypting and decrypting images using pixel manipulation. The tool allows users to modify pixel values of an image using a key to either encrypt or decrypt the image.

## Features

- **Encrypt** an image by altering its pixel values with a key.
- **Decrypt** an encrypted image using the same key.
- Supports popular image formats like `.jpg`, `.jpeg`, `.png`, and `.bmp`.

## Requirements

- Python 3.x
- Pillow library for image manipulation

## Installation

To use this tool, you'll need to install the Pillow library. You can do this by running:

```bash
pip install pillow
```

## How to Use

1. **Clone or Download** the repository to your local machine.
2. **Run the script** by navigating to the project directory and running the script with Python.
3. The program will prompt you to:
   - Choose whether to **Encrypt** or **Decrypt** an image.
   - Provide the **input path** to the image.
   - Specify the **output path** where the resulting image will be saved.
   - Enter a **key** (an integer) to modify the image pixels.

## How It Works

- **Encryption**: The key is added to each pixel’s color values (Red, Green, Blue) to make the image’s content unrecognizable.
- **Decryption**: The same key is subtracted from each pixel’s color values to restore the original image.

**Note**: This method is for demonstration purposes only and is not cryptographically secure.
