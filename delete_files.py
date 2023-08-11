import os
import shutil

# List of directory names to keep
directories_to_keep = [
    "blankets", "buddha", "buddha2", "buddha3", "buddha4", "courtyard", "imgur",
    "invincible2", "invincible4", "neonomicon", "providence", "sandcastle",
    "sandcastle2", "sandman", "sandman11", "sandman12", "sandman2", "sandman3",
    "sandman4", "sandman5", "sandman6", "sandman9", "showcase", "swamp-thing",
    "understanding-comics", "walking-dead", "walking-dead2"
]

directory_path = 'assets/img/comics'  # Update this path to your directory

# Iterate through the items in the directory
for item_name in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item_name)
    # If the item is a directory and not in the list of directories to keep, delete it
    if os.path.isdir(item_path) and item_name not in directories_to_keep:
        try:
            shutil.rmtree(item_path)
            print(f"Deleted directory: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")