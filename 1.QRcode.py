import qrcode
from PIL import Image

# Function to generate a QR code with an optional logo
def generate_qr(data, filename="qr_code.png", fill_color="red", back_color="blue", logo_path=None):
    qr = qrcode.QRCode(
        version=5,  # Increased version for more complexity
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    
    # Add data to QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR Code Image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Add logo if provided
    if logo_path:
        logo = Image.open(logo_path)
        img = img.convert("RGBA")  # Ensure it's in RGB mode for pasting

        # Resize logo to fit in QR code center
        qr_width, qr_height = img.size
        logo_size = qr_width // 4  # Logo size as a fraction of QR size
        logo = logo.resize((logo_size, logo_size))

        # Compute positioning and paste logo
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        img.paste(logo, pos, mask=logo)

    # Save and show the QR code
    img.save(filename)
    img.show()

# Example Usage
generate_qr(
    data="https://www.youtube.com/watch?v=-EKDc_99tb0&t=2s",
    filename="Euler_Theorem_QR.png",
    fill_color="red",
    back_color="blue",
    logo_path=None  # Replace with "logo.png" if you want to add a logo
)



