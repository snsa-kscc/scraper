import os

root_dir = "./folders"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)

        if "-01" in filename or "-02" in filename or "-03" in filename:

            new_filename = filename.replace(
                "-01", "").replace("-02", "").replace("-03", "")
            new_filepath = os.path.join(dirpath, new_filename)

            os.rename(filepath, new_filepath)
