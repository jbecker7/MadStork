from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # You can add a header here if you'd like
        pass

    def footer(self):
        # You can add a footer here if you'd like
        pass

def create_pdf_with_image():
    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=24)  # Adjust size as needed

    # Add a centered cell (text content)
    # The cell width is set to 0, which means it will take the full width of the page
    # The height is set to 40 for a bit of vertical spacing
    pdf.cell(0, 40, txt="Hello, World!", ln=True, align='C')

    # Image path
    image_path = 'image.jpg'

    # Get image dimensions to maintain aspect ratio
    img_width, img_height = pdf.get_image_dimensions(image_path)
    aspect_ratio = img_height / img_width

    # Image parameters
    max_width = 190
    max_height = 190 * aspect_ratio

    # Insert image
    x = (210 - max_width) / 2  # A4 width is 210 mm, adjust the x-coordinate to center the image
    pdf.image(image_path, x=x, y=pdf.get_y(), w=max_width, h=max_height)

    # Output the PDF to a file
    pdf.output("output.pdf")

if __name__ == "__main__":
    create_pdf_with_image()
