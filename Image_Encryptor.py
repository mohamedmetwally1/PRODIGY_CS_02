from PIL import Image
import os

# Function to encrypt or decrypt the image based on a key
def process_image(input_path, output_path, key, encrypt=True):
    # Open the image
    image = Image.open(input_path)
    
    # Convert the image to RGBA (with alpha channel) if not already
    image = image.convert('RGBA') if image.mode != 'RGBA' else image
    pixels = image.load()
    
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]  # Get the RGBA values
            
            if encrypt:
                # Simple encryption by shifting pixel values
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                a = (a + key) % 256  # Optional: Change alpha channel as well
            else:
                # Decrypt by reversing the shift
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                a = (a - key) % 256  # Reverse the alpha change
            
            pixels[x, y] = (r, g, b, a)  # Set the pixel back with new values

    # Save the image
    output_path = output_path if output_path.endswith(('.jpg', '.jpeg', '.png', '.bmp')) else output_path + '.png'
    image.save(output_path)

# Function to get user input for encryption or decryption
def get_input():
    print()
    print('***  IMAGE_ENCRYPTOR  ***')
    print()
    action = input("Encrypt or Decrypt (E/D): ").lower()
    input_path = input("Enter image path: ")
    output_path = input("Enter output path: ")
    key = int(input("Enter key (integer): "))
    return action, input_path, output_path, key

if __name__ == "__main__":
    action, input_path, output_path, key = get_input()

    # Ensure the input file exists
    while not os.path.exists(input_path):
        print("Invalid path.")
        input_path = input("Enter image path: ")

    # Process the image (either encrypt or decrypt based on user choice)
    process_image(input_path, output_path, key, encrypt=(action == 'e'))
    print(f"Operation complete. Saved to: {output_path}")
