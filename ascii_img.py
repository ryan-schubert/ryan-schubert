from PIL import Image

def convert_to_ascii(image_path, new_width=115, new_height=60, step_size=2):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Resize the image to the desired width and height
    resized_image = grayscale_image.resize((new_width, new_height))

    # Define ASCII characters from darkest to lightest
    ascii_chars = "@%#*+=-:. "

    # Convert each pixel to ASCII with step size for both dimensions
    ascii_image = ""
    for y in range(0, new_height, step_size):
        for x in range(0, new_width, step_size):
            pixel_value = resized_image.getpixel((x, y))
            ascii_image += ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]

        # Add a newline character after each row
        ascii_image += "\n"

    return ascii_image


def generate_svg_tspan_block(ascii_text):
    # Split the ASCII text into lines
    lines = ascii_text.split("\n")

    # Generate SVG text block with tspan tags
    svg_content = f'<text x="15" y="30" fill="#c9d1d9" class="ascii">\n'

    for i, line in enumerate(lines):
        svg_content += f'  <tspan x="15" y="{30 + i * 20}">{line}</tspan>\n'

    svg_content += '</text>'

    return svg_content

if __name__ == "__main__":
    # Replace with the path to your image
    image_path = "C:\\Users\\rschubert\\Downloads\\me.jpg"

    # Convert image to ASCII
    ascii_text = convert_to_ascii(image_path)

    # Generate SVG text block with tspan tags
    svg_content = generate_svg_tspan_block(ascii_text)

    # Print or save the SVG content
    print(svg_content)
