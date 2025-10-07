# QR Code Generator

A lightweight **Python-based QR Code Generator** that allows you to create customized QR codes with your own **themes, colours, and SVG styles**.  
Built using the [`qrcode`](https://pypi.org/project/qrcode/) library and [`Pillow`](https://pypi.org/project/Pillow/), it builds on the basic functionlity of the library, providing interactability and options for styling, scaling, and output formats.

## Features

-  Generate **QR codes** for text, URLs, or any string input.  
-  Choose from **predefined colour themes** or enter **manual HEX / named colours**.  
-  Supports **SVG** and **PNG** export options.  
-  Offers multiple **SVG factory options**:
  - `SvgImage`: basic SVG rectangles  
  - `SvgFillImage`: rectangles with background fill  
  - `SvgFragmentImage`: inline `<svg>` fragment  
  - `SvgPathImage`: path-based SVG (no background)  
  - `SvgPathFillImage`: path-based SVG with background fill  
-  Built-in **validation** for colour inputs (HEX or Pillow’s named colours).  
-  Simple CLI interface for interactive use.

## Installation

Clone the repository:

```bash
git clone https://github.com/dane679/qrcode-generator.git
cd qrcode-generator
```

## Getting started

Install the required libraries:
```bash
pip install qrcode[pil]
```
or
```bash
pip install -r requirements.txt
```

## Example Usage

Either run directly in your IDE of choice

or

Run the program in your terminal:

```bash
python main.py
```

Through the CLI you’ll be guided through:

1. Entering the text/URL to encode.

1. Choosing your output format (PNG or SVG).

1. Selecting a theme or entering custom colours.

1. Generating the final QR code file.

Example output:

![Example QR code](/exmple.png)

## Example Themes

| Theme Name | Foreground | Background |
|-------------|-------------|-------------|
| Classic     | Black       | White       |
| Midnight    | #1A1A1A     | #EAEAEA     |
| Coral       | #FF6B6B     | #FFF5F5     |
| Oceanic     | #0077B6     | #CAF0F8     |
| Forest      | #2D6A4F     | #D8F3DC     |

## Project Structure
```bash
qr_code_generator
│
├── main.py # Main script
├── requirements.txt # Dependencies
└── .gitignore # Ignored files and folders
```

## License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for full details.
