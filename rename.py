import os

folder_paths = [f for f in os.listdir('./resize') if not f.startswith('.')]
base_folder = './resize'

for i in folder_paths:

    folder_path = os.path.join(base_folder, i)

    for filename in [f for f in os.listdir(folder_path) if not f.startswith('.')]:
        base_filename = os.path.splitext(filename)[0]
        file_extension = os.path.splitext(filename)[1]
        second_last_char = base_filename[-2]

        if second_last_char == '_':
            new_base_filename = base_filename[:-
                                              2] + '-' + base_filename[-1]
            new_filename = i + new_base_filename + file_extension
            os.rename(os.path.join(folder_path, filename),
                      os.path.join(folder_path, new_filename))
