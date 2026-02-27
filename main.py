import qrcode
import uuid
import os

# File to store previously generated codes
HISTORY_FILE = "generated_codes.txt"

def get_unique_id():
    # Load existing IDs to prevent repeats
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            used_ids = set(line.strip() for line in f)
    else:
        used_ids = set()

    while True:
        # Generate a random unique ID
        new_id = str(uuid.uuid4())
        if new_id not in used_ids:
            # Save the new ID immediately
            with open(HISTORY_FILE, "a") as f:
                f.write(new_id + "\n")
            return new_id

def generate_qr():
    unique_data = get_unique_id()
    
    # Create the QR code object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(unique_data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_{unique_data[:8]}.png"
    img.save(filename)
    
    print(f"Success! Generated unique QR: {filename}")

if __name__ == "__main__":
    generate_qr()