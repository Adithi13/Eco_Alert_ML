import pandas as pd

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


# Generate image paths
image_paths = []
for obj in objects:
    paths = [f'images/{obj}/Image_{i}' for i in range(1, 51)]  # No file extension added
    image_paths.append(paths)


# Create the DataFrame
data = {
    "Category": categories,
    "Object": objects,
    "Image_Paths": image_paths
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save DataFrame to CSV
df.to_csv('updated_dataset.csv', index=False)