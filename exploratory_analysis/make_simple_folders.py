import os

directory = './resize'
base_directory = './'
unsorted_file_list = [f for f in os.listdir(
    directory) if not f.startswith('.')]
file_list = sorted(unsorted_file_list)


for i in range(0, len(file_list)+1, 5):
    folder_name = "folder_" + str(i//5 + 1)
    path = os.path.join(base_directory, folder_name)
    if not os.path.exists(path):
        os.mkdir(folder_name)
    for file_name in file_list[i:i+5]:
        source = os.path.join(directory, file_name)
        destination = os.path.join(base_directory, folder_name, file_name)
        os.rename(source, destination)
