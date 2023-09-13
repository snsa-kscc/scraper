import os

directory = "./assets/resize"
abs_directory = os.path.abspath(directory)

files = [f for f in os.listdir(directory) if not f.startswith('.')]

for filename in files:
    if "_" in filename:
        new_filename = filename.replace("_", "-", 1)
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, new_filename))

print("Files renamed successfully.")
