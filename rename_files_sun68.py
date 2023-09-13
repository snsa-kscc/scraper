import os
import re

directory = "./assets/resize"

files = [f for f in os.listdir(directory) if not f.startswith('.')]

pattern = re.compile(r'^(Z\d+_\d+)_[BCD](\.jpg)$')

count_mapping = {'B': 2, 'C': 3, 'D': 4}

for filename in files:
    match = pattern.match(filename)
    if match:
        base_name = match.group(1)
        extension = match.group(2)
        letter = filename.split('_')[2][0]
        new_count = count_mapping.get(letter)
        new_filename = f"{base_name}_{new_count}{extension}"
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, new_filename))
    else:
        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}_1{extension}"
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, new_filename))

print("Files renamed successfully.")
