import os
import shutil

sku_model_dict = {'S70665-3': 'SAUCONY-ORIGINALSShadow-5000-muska-tenisica-S70665-3',
                  'S1044-668': 'SAUCONY-ORIGINALSJazz-Original-zenska-tenisica-S1044-668',
                  'S60530-21': 'SAUCONY-ORIGINALSJazz-Triple-zenska-tenisica-S60530-21',
                  'S70665-14': 'SAUCONY-ORIGINALSShadow-5000-muska-tenisica-S70665-14',
                  'S70700-1': 'SAUCONY-ORIGINALSShadow-6000-unisex-tenisica-S70700-1',
                  'S60690-1': 'SAUCONY-ORIGINALSJazz-Triple-zenska-tenisica-S60690-1',
                  'S60690-2': 'SAUCONY-ORIGINALSJazz-Triple-zenska-tenisica-S60690-2'}

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
