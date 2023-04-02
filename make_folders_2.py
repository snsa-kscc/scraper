import os
import shutil

sku_model_dict = {'S10440-37': 'SAUCONY-Freedom-Iso-2-zenska-tenisica-S10440-37',
                  'S10447-2': 'SAUCONY-Clarion-zenska-tenisica-S10447-2',
                  'S10462-36': 'SAUCONY-Triumph-Iso-5-zenska-tenisica-S10462-36',
                  'S10464-37': 'SAUCONY-Guide-Iso-2-zenska-tenisica-S10464-37',
                  'S10464-42': 'SAUCONY-Guide-Iso-2-zenska-tenisica-S10464-42',
                  'S10492-41': 'SAUCONY-Jazz-21-zenska-tenisica-S10492-41',
                  'S20410-36': 'SAUCONY-Liberty-Iso-muska-tenisica-S20410-36',
                  'S20447-2': 'SAUCONY-Clarion-muska-tenisica-S20447-2',
                  'S20447-37': 'SAUCONY-Clarion-muska-tenisica-S20447-37',
                  'S20462-37': 'SAUCONY-Triumph-Iso-5-muska-tenisica-S20462-37',
                  'S20462-41': 'SAUCONY-Triumph-Iso-5-muska-tenisica-S20462-41',
                  'S20464-37': 'SAUCONY-Guide-Iso-2-muska-tenisica-S20464-37',
                  'S20467-36': 'SAUCONY-Kinvara-10-muska-tenisica-S20467-36',
                  'S20483-36': 'SAUCONY-Peregrine-Iso-muska-tenisica-S20483-36',
                  'S20492-36': 'SAUCONY-Jazz-21-muska-tenisica-S20492-36',
                  'S60368-112': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-112',
                  'S60368-61': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-61',
                  'S60368-62': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-62',
                  'S60368-65': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-65',
                  'S60368-66': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-66',
                  'S60368-67': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-67',
                  'S60368-71': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-71',
                  'S60368-92': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-92',
                  'S60368-97': 'SAUCONY-Jazz-Original-Vintage-zenska-tenisica-S60368-97',
                  'S60405-17': 'SAUCONY-Shadow-5000-Vintage-zenska-tenisica-S60405-17',
                  'S70368-48': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-48',
                  'S70368-52': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-52',
                  'S70368-56': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-56',
                  'S70368-81': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-81',
                  'S70368-87': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-87',
                  'S70404-11': 'SAUCONY-Shadow-5000-Vintage-muska-tenisica-S70404-11',
                  'S70424-7': 'SAUCONY-Shadow-Original-Vintage-muska-tenisica-S70424-7',
                  'S70424-8': 'SAUCONY-Shadow-Original-Vintage-unisex-tenisica-S70424-8',
                  'S70437-1': 'SAUCONY-Azura-unisex-tenisica-S70437-1',
                  'S70441-1': 'SAUCONY-Shadow-6000-unisex-tenisica-S70441-1',
                  'S70480-1': 'SAUCONY-Shadow-5000-unisex-tenisica-S70480-1',
                  'SA81540-HB': 'SAUCONY-Hydralite-Tank-z-maja-SA81540-HB',
                  'SAM800057-DGH': 'SAUCONY-Mens-Life-On-The-Run-Cdwn-Ls-m-maja-SAM800057-DGH',
                  'SAM800058-DGH': 'SAUCONY-Mens-Life-On-The-Run-Cdwn-Jgr-m-hlace-SAM800058-DGH',
                  'SAM800188-BK': 'SAUCONY-Cooldown-Woven-Pant-m-hlace-SAM800188-BK',
                  'SAW800104-HBP': 'SAUCONY-Impulse-Crop-Top-z-top-SAW800104-HBP',
                  'SAW800148-HBP': 'SAUCONY-Bullet-Tight-Short-20-z-kr-hlace-SAW800148-HBP',
                  'SAW800253-LPRA': 'SAUCONY-Ra-Endorphine-Singlet-z-maja-SAW800253-LPRA',
                  'SAW800259-DGHBK': 'SAUCONY-Cooldown-Jacket-z-jakna-SAW800259-DGHBK',
                  'SAW800261-BK': 'SAUCONY-Cooldown-Woven-Pant-z-hlace-SAW800261-BK',
                  'SK161015': 'SAUCONY-Jazz-Double-Hl-djecja-tenisica-SK161015',
                  'SK260996': 'SAUCONY-S-Jazz-Original-Vintage-djecja-tenisica-SK260996',
                  'SK261010': 'SAUCONY-Jazz-Double-Hl-djecja-tenisica-SK261010'}

picture_folder_path = './resize'

for sku, model in sku_model_dict.items():

    model_folder_path = os.path.join(picture_folder_path, model)
    if not os.path.exists(model_folder_path):
        os.makedirs(model_folder_path)

    sku_picture_files = [f for f in os.listdir(
        picture_folder_path) if f.startswith(sku)]

    for picture_file in sku_picture_files:
        picture_file_path = os.path.join(picture_folder_path, picture_file)
        shutil.move(picture_file_path, model_folder_path)
