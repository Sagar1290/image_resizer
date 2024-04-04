import os
from PIL import Image, ImageDraw
import face_recog
import cv2

def resize_and_crop_face_centered(input_image, output_size):
    # image = Image.open(input_image)                   #if have bunch of images coming from folder then uncomment this line and comment next line
    image = input_image
    original_width, original_height = image.size

    # Calculate new dimensions while maintaining aspect ratio
    if original_width < original_height:
        new_width = output_size
        new_height = int(original_height * (output_size / original_width))
    else:
        new_height = output_size
        new_width = int(original_width * (output_size / original_height))

    # Resize the image
    
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    temp_image = resized_image
    temp_filepath = os.path.join(os.getcwd(), "temp_resized.jpg")
    resized_image.save(temp_filepath)

    # Extract facial recognition data
    coords = face_recog.get_facial_coords(temp_filepath)

    if not coords:
        return None
    
    os.remove(temp_filepath)
    x, y, w, h = coords['x'], coords['y'], coords['w'], coords['h']

    draw = ImageDraw.Draw(temp_image)
    image_with_face = draw.rectangle([x, y, x + w, y + h], outline="red", width=2)
    

    # Calculate centered coordinates for the 512x512 crop
    center_x = x + (w // 2)
    center_y = y + (h // 2)

    if(new_height > new_width):
        crop_start_x = 0
        crop_start_y = int(max(0, center_y - output_size // 2))        
    else:
        crop_start_y = 0
        crop_start_x = int(max(0, center_x - output_size // 2))

    crop_end_x = crop_start_x + output_size
    crop_end_y = crop_start_y + output_size

    # Crop the image centered on the face
    cropped_image = resized_image.crop((crop_start_x, crop_start_y, crop_end_x, crop_end_y))

    return image_with_face, cropped_image




####################################################################################################
# make a directory named input_images with all the images in it and uncomment below lines of code 

# input_folder = "input_images"
# output_folder = "output_images"
# os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

# for filename in os.listdir(input_folder):
#     image_path = os.path.join(input_folder, filename)

#     if not os.path.isfile(image_path):
#         print(f"Error processing {filename}")
#         continue  # Skip to the next iteration

#     output_size = int(input("Enter desired output size (integer): "))

#     resized_image = resize_and_crop_face_centered(image_path, output_size)

#     if resized_image:  # Check if a face is detected
#         # Create the subfolder within the output folder using the output size (converted to string for path joining)
#         output_subfolder = os.path.join(output_folder, str(output_size))
#         os.makedirs(output_subfolder, exist_ok=True)  # Create subfolder if it doesn't exist

#         # Construct the output path within the subfolder
#         output_path = os.path.join(output_subfolder, filename)
#         resized_image.save(output_path)
#         print(f"Successfully resized and cropped: {filename} (saved to {output_subfolder})")
#     else:
#         print(f"No face detected in {filename}")


# print("Images resized and cropped successfully!")
