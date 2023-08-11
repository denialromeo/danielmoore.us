import re

file_path = 'about.md'  # Update this path to your file

# Regular expression pattern to find full filenames, including parent directories, ending with .jpg, .jpeg, or .png
pattern = r'\b[\w/]+\.(?:jpg|jpeg|png)\b'

# Open the file and read the content using UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    # Find all occurrences of the pattern in the content
    full_filenames = re.findall(pattern, content)
    for filename in full_filenames:
        print(filename)