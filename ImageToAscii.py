from PIL import Image

def image_to_dots(image_path, width=100):
    # Open image and convert it to grayscale
    img = Image.open(image_path).convert('L')

    # Resize image while maintaining aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))

    # Define the characters for different grayscale levels
    chars = "@%#*+=-:. "
    scale = 255 // (len(chars) - 1)
    
    # Process pixels and map to characters
    result = ""
    for y in range(img.height):
        for x in range(img.width):
            gray_value = img.getpixel((x, y))
            result += chars[gray_value // scale]
        result += "\n"

    return result

# Load and display the image using dots
#image_path = r"C:\Users\HP\Downloads\professional_photo_4.jpg"  # Use raw string for Windows path
image_path = r"flower.jpg"
print(image_to_dots(image_path))
