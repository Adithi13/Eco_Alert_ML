# import os
# import pandas as pd
# from PIL import Image
# import numpy as np

# # List of categories
# categories = [
#     "weapons/firearms", "weapons/firearms", "weapons/firearms", "weapons/firearms",
#     "weapons/bladed_weapons", "weapons/bladed_weapons", "weapons/bladed_weapons",
#     "hunting_tools/traps", "hunting_tools/traps", "hunting_tools/traps",
#     "hunting_tools/nets", "hunting_tools/spears_harpoons", "hunting_tools/spears_harpoons",
#     "vehicles", "vehicles", "vehicles",
#     "equipment", "equipment",
#     "camouflage_gear", "camouflage_gear", "camouflage_gear",
#     "animal_parts/carcasses", "animal_parts/carcasses",
#     "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts",
#     "animal_parts/processed_products", "animal_parts/processed_products", "animal_parts/processed_products",
#     "miscellaneous/containers", "miscellaneous/containers", "miscellaneous/containers",
#     "miscellaneous/poison",
#     "fishing_gear", "fishing_gear",
#     "poaching_activities/camps", "poaching_activities/camps", "poaching_activities/camps",
#     "poaching_activities/tools", "poaching_activities/tools",
#     "technology", "communication_devices", "communication_devices"
# ]

# # List of objects
# objects = [
#     "rifle", "shotgun", "handgun", "automatic_weapon",
#     "machete", "knife", "axe",
#     "steel_jaw_trap", "cable_snare", "pitfall_trap",
#     "bird_net", "spear", "harpoon",
#     "off_road_vehicle", "motorbike", "boat",
#     "night_vision_equipment", "thermal_imaging_equipment",
#     "camouflage_clothing", "camouflage_tent", "camouflage_hide",
#     "animal_carcass", "animal_skin",
#     "ivory", "rhino_horn", "tiger_bone", "shark_fin", "bear_paw",
#     "animal_fur_product", "leather_product", "traditional_medicine_ingredient",
#     "cooler", "large_sack", "bag",
#     "poison_container",
#     "dynamite", "poisonous_bait",
#     "tent", "cooking_equipment", "illegal_campsite",
#     "bone_saw", "meat_cleaver",
#     "drone", "walkie_talkie", "satellite_phone"
# ]

# # Generate image paths
# image_paths = []
# for obj in objects:
#     paths = [f'images/{obj}/Image_{i}' for i in range(1, 51)]  # No file extension added
#     image_paths.append(paths)

# # Create the DataFrame
# data = {
#     "Category": categories,
#     "Object": objects,
#     "Image_Paths": image_paths
# }
# df = pd.DataFrame(data)

# def find_image_file(base_path):
#     for ext in ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']:
#         file_path = base_path + ext
#         if os.path.isfile(file_path):
#             return file_path
#     return None

# def image_to_array(image_path):
#     image_file = find_image_file(image_path)
#     if image_file is None:
#         print(f"File not found: {image_path}")
#         return None
#     with Image.open(image_file) as img:
#         img_array = np.array(img)
#     return img_array

# def process_images(image_paths):
#     images = [image_to_array(path) for path in image_paths]
#     images = [img for img in images if img is not None]
#     return images

# def create_dataset_with_images(df):
#     all_images = []
#     all_categories = []
#     all_objects = []

#     for index, row in df.iterrows():
#         category = row['Category']
#         object_name = row['Object']
#         image_paths = eval(row['Image_Paths'])
#         images = process_images(image_paths)

#         if not images:
#             continue

#         all_images.extend(images)
#         all_categories.extend([category] * len(images))
#         all_objects.extend([object_name] * len(images))

#     image_data = {
#         'Category': all_categories,
#         'Object': all_objects,
#         'Image': all_images
#     }

#     new_df = pd.DataFrame(image_data)
#     return new_df

# # Set the base file location
# base_file_location = r'C:\Users\pc\Desktop\Eco_Alert_ML\images'

# # Update image paths with the base file location
# df['Image_Paths'] = df['Image_Paths'].apply(lambda paths: [os.path.join(base_file_location, path) for path in paths])

# # Create a new DataFrame with images
# new_df = create_dataset_with_images(df)

# # Save the new DataFrame to a CSV file (optional)
# new_df.to_csv('dataset_with_images.csv', index=False)

# # Display the new DataFrame (optional)
# print(new_df.head())
import os
import pandas as pd
from PIL import Image
import numpy as np

# List of categories
categories = [
    "weapons/firearms", "weapons/firearms", "weapons/firearms", "weapons/firearms",
    "weapons/bladed_weapons", "weapons/bladed_weapons", "weapons/bladed_weapons",
    "hunting_tools/traps", "hunting_tools/traps", "hunting_tools/traps",
    "hunting_tools/nets", "hunting_tools/spears_harpoons", "hunting_tools/spears_harpoons",
    "vehicles", "vehicles", "vehicles",
    "equipment", "equipment",
    "camouflage_gear", "camouflage_gear", "camouflage_gear",
    "animal_parts/carcasses", "animal_parts/carcasses",
    "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts", "animal_parts/body_parts",
    "animal_parts/processed_products", "animal_parts/processed_products", "animal_parts/processed_products",
    "miscellaneous/containers", "miscellaneous/containers", "miscellaneous/containers",
    "miscellaneous/poison",
    "fishing_gear", "fishing_gear",
    "poaching_activities/camps", "poaching_activities/camps", "poaching_activities/camps",
    "poaching_activities/tools", "poaching_activities/tools",
    "technology", "communication_devices", "communication_devices"
]

# List of objects
objects = [
    "rifle", "shotgun", "handgun", "automatic_weapon",
    "machete", "knife", "axe",
    "steel_jaw_trap", "cable_snare", "pitfall_trap",
    "bird_net", "spear", "harpoon",
    "off_road_vehicle", "motorbike", "boat",
    "night_vision_equipment", "thermal_imaging_equipment",
    "camouflage_clothing", "camouflage_tent", "camouflage_hide",
    "animal_carcass", "animal_skin",
    "ivory", "rhino_horn", "tiger_bone", "shark_fin", "bear_paw",
    "animal_fur_product", "leather_product", "traditional_medicine_ingredient",
    "cooler", "large_sack", "bag",
    "poison_container",
    "dynamite", "poisonous_bait",
    "tent", "cooking_equipment", "illegal_campsite",
    "bone_saw", "meat_cleaver",
    "drone", "walkie_talkie", "satellite_phone"
]

# Set the base file location
base_file_location = r'C:\Users\pc\Desktop\Eco_Alert_ML\images'

# Generate image paths with correct file extension
image_paths = []
for obj in objects:
    paths = [os.path.join(base_file_location, obj, f'Image_{i}.jpg') for i in range(1, 51)]
    image_paths.append(paths)

# Create the DataFrame
data = {
    "Category": categories,
    "Object": objects,
    "Image_Paths": image_paths
}
df = pd.DataFrame(data)

def find_image_file(base_path):
    for ext in ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']:
        file_path = base_path + ext
        if os.path.isfile(file_path):
            return file_path
    return None

def image_to_array(image_path):
    print(f"Checking path: {image_path}")  # Debugging print
    image_file = find_image_file(image_path)
    if image_file is None:
        print(f"File not found: {image_path}")
        return None
    print(f"Found file: {image_file}")  # Debugging print
    try:
        with Image.open(image_file) as img:
            img_array = np.array(img)
        return img_array
    except Exception as e:
        print(f"Error opening image {image_file}: {e}")
        return None

def process_images(image_paths):
    images = [image_to_array(path) for path in image_paths]
    images = [img for img in images if img is not None]
    return images

def create_dataset_with_images(df):
    all_images = []
    all_categories = []
    all_objects = []

    for index, row in df.iterrows():
        category = row['Category']
        object_name = row['Object']
        image_paths = row['Image_Paths']
        images = process_images(image_paths)

        if not images:
            print(f"No images found for {object_name}")
            continue

        all_images.extend(images)
        all_categories.extend([category] * len(images))
        all_objects.extend([object_name] * len(images))

    image_data = {
        'Category': all_categories,
        'Object': all_objects,
        'Image': all_images
    }

    new_df = pd.DataFrame(image_data)
    return new_df

# Update image paths with the base file location
df['Image_Paths'] = df['Image_Paths'].apply(lambda paths: [os.path.join(base_file_location, path) for path in paths])

# Create a new DataFrame with images
new_df = create_dataset_with_images(df)

# Save the new DataFrame to a CSV file (optional)
new_df.to_csv('dataset_with_images.csv', index=False)

# Display the new DataFrame (optional)
print(new_df.head())
