import os
import shutil

sku_model_dict = {'Z43203-44': 'SUN68-Ally-Bright-Nylon-zenske-tenisice-Z43203-44',
                  'Z43202-31': 'SUN68-Ally-Gold-Girl-zenske-tenisice-Z43202-31',
                  'Z43201-77': 'SUN68-Ally-Solid-zenske-tenisice-Z43201-77',
                  'Z43201-34': 'SUN68-Ally-Solid-zenske-tenisice-Z43201-34',
                  'Z43201-09': 'SUN68-Ally-Solid-zenske-tenisice-Z43201-09',
                  'Z43104-74': 'SUN68-Tom-Classic-muske-tenisice-Z43104-74',
                  'Z43104-07': 'SUN68-Tom-Classic-muske-tenisice-Z43104-07',
                  'Z43102-11': 'SUN68-Tom-Fluo-muske-tenisice-Z43102-11',
                  'Z43102-07': 'SUN68-Tom-Fluo-muske-tenisice-Z43102-07',
                  'Z43101-74': 'SUN68-Tom-Solid-muske-tenisice-Z43101-74',
                  'Z43101-70': 'SUN68-Tom-Solid-muske-tenisice-Z43101-70',
                  'Z43101-08': 'SUN68-Tom-Solid-muske-tenisice-Z43101-08',
                  'Z43101-07': 'SUN68-Tom-Solid-muske-tenisice-Z43101-07',
                  'Z43101-01': 'SUN68-Tom-Solid-muske-tenisice-Z43101-01'}

picture_folder_path = './assets/resize'

for sku, model in sku_model_dict.items():

    model_folder_path = os.path.join(picture_folder_path, model)
    if not os.path.exists(model_folder_path):
        os.makedirs(model_folder_path)

    sku_picture_files = [f for f in os.listdir(
        picture_folder_path) if f.startswith(sku)]

    for picture_file in sku_picture_files:
        picture_file_path = os.path.join(picture_folder_path, picture_file)
        shutil.move(picture_file_path, model_folder_path)
