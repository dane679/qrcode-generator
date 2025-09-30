import qrcode
import qrcode.image.svg
from PIL import ImageColor
import re

def gen_qr(text, 
           file_name, 
           ffill = None, 
           bfill = None, 
           theme=None,  
           svg_mode = True,
           factory = qrcode.image.svg.SvgPathFillImage
        ):
    
    ext = ".svg" if svg_mode else ".png"
    if not file_name.endswith(ext):
        file_name += ext

    
    # Applies given theme
    if theme and theme in THEMES:
        ffill = THEMES[theme]["fill"]
        bfill = THEMES[theme]["back"]
        print(f"[Theme Mode] Using theme '{theme}': fill=#{ffill}, back=#{bfill}")

    if svg_mode == True:
        print("svg mode enabled\n")
        # factory = qrcode.image.svg.SvgPathFillImage
        qr = qrcode.QRCode(
            image_factory = factory,
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        svg_img = qr.make_image()

        svg_img.save(f"{file_name}")
        with open(f"{file_name}", "r") as qr_img:
            content = qr_img.read()
        
        # Handle replacements based on available values
        if ffill and bfill:
            content = content.replace("#000000", f"#{ffill}")  
            content = content.replace("#ffffff", f"#{bfill}")  
            content = content.replace("white", f"#{bfill}")  
            content = content.replace("svg:rect", f'svg:rect fill="#{ffill}"')  
            print(f"Using both: fill=#{ffill}, back=#{bfill}")
        elif ffill:
            content = content.replace("#000000", f"#{ffill}")  
            content = content.replace("svg:rect", f'svg:rect fill="#{ffill}"')  
            print(f"Using fill only: #{ffill}")
        elif bfill:
            content = content.replace("#ffffff", f"#{bfill}")  
            content = content.replace("white", f"#{bfill}")  
            print(f"Using back only: #{bfill}")

        else:
            print("[Default Mode] Using default black and white")

        # Always ensure crisp edges
        content = content.replace("svg ", 'svg shape-rendering="crispEdges" ')


        with open(f"{file_name}", "w+") as qr_img:
            qr_img.write(content)
        print(f"File made")
        
    else:
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )

        qr.add_data(text)
        qr.make(fit = True)

        if ffill and bfill:
            img = qr.make_image(fill_color=f"#{ffill}", back_color=f"#{bfill}")
            print(f"Using both: fill=#{ffill}, back=#{bfill}")
        elif ffill:
            img = qr.make_image(fill_color=f"#{ffill}")
            print(f"Using fill only: #{ffill}")
        elif bfill:
            img = qr.make_image(back_color=f"#{bfill}")
            print(f"Using back only: #{bfill}")
        else:
            img = qr.make_image()

        img.save(file_name)
        print(f"File stored as: {file_name}")

def validate_color_input(color):
    # Validate if the input is a valid hex code (without '#') or a Pillow named color.
    # HEX: must be 3 or 6 hex digits
    hex_pattern = re.compile(r'^[0-9A-Fa-f]{6}$|^[0-9A-Fa-f]{3}$')

    if hex_pattern.fullmatch(color):
        return True

    # Try named colors (Pillow built-in)
    try:
        ImageColor.getrgb(color)  # If invalid, raises ValueError
        return True
    except ValueError:
        return False

### add svg, colour contrast checker and basic interactive features with a custom tkinter UI.

def ask_for_colors():
    # Optional: ask if user wants to see supported named colors
    show_list = input("Would you like to see the list of supported named colors? (y/n): ").strip().lower()
    if show_list in ["", "y", "yes"]:
        named_colors = sorted(ImageColor.colormap.keys())
        print(f"\nPillow supports {len(named_colors)} named colors:")
        # Print in a wrapped format for readability
        for i, color in enumerate(named_colors, 1):
            print(f"{color:15}", end=" ")
            if i % 6 == 0:  # 6 per line
                print()
        print("\n")  

# Theme presets
THEMES = {
    "neon": {
        "fill": "78ff9b",   
        "back": "282435"    
    },
    "nightlight": {
        "fill": "F5F86D",   
        "back": "02193A"    
    },
    "sunset": {
        "fill": "FF4500", 
        "back": "FFDAB9"
    },
    "midnight": {
      "fill": "9AB8FF",
      "back": "0B132B"
    },
    "ember": {
      "fill": "FF6B35",
      "back": "1B1B1B"
    },
    "citrus": {
      "fill": "FFDD00",
      "back": "003300"
    },
    "blaze": {
      "fill": "FFD166",
      "back": "2E0F00"
    },
    "ocean": {
      "fill": "00E5FF",
      "back": "001F33"
    },
    "ice": {
      "fill": "B3F0FF",
      "back": "0A2A3A"
    },
    "mint": {
      "fill": "A8FFDA",
      "back": "1E2E1E"
    },
    "Amethyst": {
      "fill": "E2B6FF",
      "back": "2C1A47"
    },
    "peach": {
      "fill": "FFBCB3",
      "back": "2A1E1A"
    },
    "clay": {
      "fill": "EED9C4",
      "back": "3A2C1A"
    }
}
### in gui add seperate customisable file for themes.

SVG_FACTORIES = {
    "1": {
        "label": "svg",
        "factory": qrcode.image.svg.SvgImage,
        "desc": "Basic SVG with rectangles, no background."
    },
    "2": {
        "label": "svg_fill",
        "factory": qrcode.image.svg.SvgFillImage,
        "desc": "SVG with rectangles and filled background."
    },
    "3": {
        "label": "fragment",
        "factory": qrcode.image.svg.SvgFragmentImage,
        "desc": "Only the <svg> fragment (inline-friendly, no background)."
    },
    "4": {
        "label": "path",
        "factory": qrcode.image.svg.SvgPathImage,
        "desc": "SVG defined using paths, no background."
    },
    "5": {
        "label": "path_fill",
        "factory": qrcode.image.svg.SvgPathFillImage,
        "desc": "SVG defined with paths and a background fill."
    },
}
    

# Main function for CLI interaction
def main():
    print("\nQR Code Generator")
    print("=================")
    print("Choose an option:")
    print("1. Generate PNG QR Code")
    print("2. Generate SVG QR Code (Default)")
    choice = input("Enter 1 or 2 (or press Enter to use default): ").strip()

    # Keep asking until user enters text
    while True:
        text = input("Enter the text/URL to encode: ").strip()
        if text:
            break
        print("No text entered. Please try again.")

    # Ask for filename
    file_name = input("Enter output file name (e.g. myqr): ").strip()
    if not file_name:
        file_name = "qrcode"

    # Show available themes
    print("\nAvailable themes:")
    theme_list = list(THEMES.keys())
    for i, name in enumerate(theme_list, start=1):
        print(f"  {i}. {name}")
    print("  (Leave empty for manual colors).")

    ffill, bfill, theme = None, None, None  # defaults

    while True:
        theme_choice = input("Enter theme name or number: ").strip().lower()

        # Case 1: Blank input → manual colors
        if not theme_choice:
            ask_for_colors()
            while True:
                ffill = input("Enter foreground color with HEX (e.g. 000000), named colours or press Enter for default: ").strip()
                if not ffill or validate_color_input(ffill):
                    break
                print("Invalid color format. Try again (must be 3 or 6 hex digits), or a named colors (like 'black', 'white'")
                ask_for_colors()

            while True:
                bfill = input("Enter background color with HEX (e.g. 000000), named colours or press Enter for default: ").strip()
                if not bfill or validate_color_input(bfill):
                    break
                print("Invalid color format. Try again (must be 3 or 6 hex digits), or a named colors (like 'black', 'white'")
                ask_for_colors()


            theme = None
            print(f"Using manual colors: fill=#{ffill or '000000'}, back=#{bfill or 'ffffff'}")
            break  

        # Case 2: Number input
        if theme_choice.isdigit():
            idx = int(theme_choice) - 1
            if 0 <= idx < len(theme_list):
                theme = theme_list[idx]
                ffill = THEMES[theme]["fill"]
                bfill = THEMES[theme]["back"]
                print(f"Using theme '{theme}': fill=#{ffill}, back=#{bfill}")
                break
            else:
                print("Invalid theme number. Try again.")

        # Case 3: Name input
        elif theme_choice in THEMES:
            theme = theme_choice
            ffill = THEMES[theme]["fill"]
            bfill = THEMES[theme]["back"]
            print(f"Using theme '{theme}': fill=#{ffill}, back=#{bfill}")
            break
        else:
            print("Invalid theme name. Try again.")

    if choice == "1":
        svg_mode = False
        image_factory = None
    else:
        svg_mode = True
        # Ask for SVG factory type
        print("\nChoose SVG output type:")
        for key, data in SVG_FACTORIES.items():
            print(f"  {key}. {data['label']} - {data['desc']}")
        while True:
            svg_choice = input("Enter SVG type number: ").strip()
            if svg_choice in SVG_FACTORIES:
                factory_label = SVG_FACTORIES[svg_choice]["label"]
                image_factory = SVG_FACTORIES[svg_choice]["factory"]
                print(f"Using SVG factory: {factory_label}")
                break
            else:
                print("Invalid choice. Try again.")

    # Call generator
    gen_qr(
        text=text,
        file_name=file_name,
        ffill=ffill,
        bfill=bfill,
        theme=theme,
        svg_mode=svg_mode,
        factory = image_factory
    )
    ### in gui contast checker
    print(f"\nQR Code generated successfully as '{file_name}{'.svg' if svg_mode else '.png'}'.")

# Run if script executed
if __name__ == "__main__":
    main()
