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

## Getting started

Install the required libraries:
```bash
pip install qrcode[pil]
```
or
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for full details.
