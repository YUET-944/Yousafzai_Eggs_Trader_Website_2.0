from PIL import Image

def remove_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is near-white
        if item[0] > 210 and item[1] > 210 and item[2] > 210:
            # Fully transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print("Saved to", output_path)

remove_background("frontend/src/assets/logo.jpg", "frontend/src/assets/logo.png")
