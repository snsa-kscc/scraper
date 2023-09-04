import os
import shutil

sku_model_dict = {'S70424-8': 'SAUCONY-Shadow-Original-Vintage-unisex-tenisica-S70424-8',
                  'S70368-203': 'SAUCONY-Jazz-Original-Vintage-muska-tenisica-S70368-203',
                  'SAU800034-BK': 'SAUCONY-Solstice-Neck-Gaiter-ovratnik-SAU800034-BK',
                  'S10654-66': 'SAUCONY-Guide-14-zenska-tenisica-S10654-66',
                  'S20672-1': 'SAUCONY-Excursion-Tr15-Gtx-muska-tenisica-S20672-1',
                  'S10723-16': 'SAUCONY-Kinvara-13-zenska-tenisica-S10723-16',
                  'S70613-13': 'SAUCONY-Jazz-81-muska-tenisica-S70613-13',
                  'S10729-125': 'SAUCONY-Ride-15-zenska-tenisica-S10729-125',
                  'S20687-84': 'SAUCONY-Endorphin-Pro-2-muska-tenisica-S20687-84',
                  'SAW800408-SD': 'SAUCONY-Elite-Bra-Top-z-top-SAW800408-SD',
                  'SAW800412-SD': 'SAUCONY-Elite-Boy-Short-z-kr-hlace-SAW800412-SD',
                  'SAW800417-SD': 'SAUCONY-Elite-Tight-z-hlace-SAW800417-SD',
                  'S10729-30': 'SAUCONY-Ride-15-zenska-tenisica-S10729-30',
                  'S10813-10': 'SAUCONY-Endorphin-Shift-3-zenska-tenisica-S10813-10',
                  'S10813-65': 'SAUCONY-Endorphin-Shift-3-zenska-tenisica-S10813-65',
                  'S10838-25': 'SAUCONY-Peregrine-13-zenska-tenisica-S10838-25',
                  'S20775-25': 'SAUCONY-Ride-15-Tr-muska-tenisica-S20775-25',
                  'S10720-86': 'SAUCONY-Tempus-zenska-tenisica-S10720-86',
                  'SAM800313-UB': 'SAUCONY-Elite-Short-Sleeve-m-t-maja-SAM800313-UB',
                  'SAM800315-UB': 'SAUCONY-Elite-Split-Short-m-kr-hlace-SAM800315-UB',
                  'SAM800316-UB': 'SAUCONY-Elite-Tight-Short-m-kr-hlace-SAM800316-UB',
                  'SAM800317-UB': 'SAUCONY-Elite-Tight-m-tajce-SAM800317-UB',
                  'SAM800320-UB': 'SAUCONY-Elite-Singlet-m-maja-SAM800320-UB',
                  'SAW800407-UB': 'SAUCONY-Elite-Singlet-z-maja-SAW800407-UB',
                  'SAW800408-UB': 'SAUCONY-Elite-Bra-Top-z-top-SAW800408-UB',
                  'SAW800409-UB': 'SAUCONY-Endorphin-Elite-Crop-Top-z-top-SAW800409-UB',
                  'SAW800410-UB': 'SAUCONY-Endorphin-Elite-Brief-Short-z-kr-hlace-SAW800410-UB',
                  'SAW800412-UB': 'SAUCONY-Elite-Boy-Short-z-kr-hlace-SAW800412-UB',
                  'SAW800413-UB': 'SAUCONY-Elite-Short-Sleeve-z-t-maja-SAW800413-UB',
                  'SAW800417-UB': 'SAUCONY-Elite-Tight-z-hlace-SAW800417-UB',
                  'S10838-30': 'SAUCONY-Peregrine-13-zenska-tenisica-S10838-30',
                  'S10838-75': 'SAUCONY-Peregrine-13-zenska-tenisica-S10838-75',
                  'S20838-30': 'SAUCONY-Peregrine-13-muska-tenisica-S20838-30',
                  'S10823-36': 'SAUCONY-Kinvara-14-zenska-tenisica-S10823-36',
                  'S10823-60': 'SAUCONY-Kinvara-14-zenska-tenisica-S10823-60',
                  'S10830-30': 'SAUCONY-Ride-16-zenska-tenisica-S10830-30',
                  'S10881-32': 'SAUCONY-Triumph-21-zenska-tenisica-S10881-32',
                  'S20755-75': 'SAUCONY-Endorphin-Pro-3-muska-tenisica-S20755-75',
                  'S20813-22': 'SAUCONY-Endorphin-Shift-3-muska-tenisica-S20813-22',
                  'S20823-33': 'SAUCONY-Kinvara-14-muska-tenisica-S20823-33',
                  'S20830-32': 'SAUCONY-Ride-16-muska-tenisica-S20830-32',
                  'S20881-21': 'SAUCONY-Triumph-21-muska-tenisica-S20881-21',
                  'S20881-60': 'SAUCONY-Triumph-21-muska-tenisica-S20881-60',
                  'S20810-34': 'SAUCONY-Guide-16-muska-tenisica-S20810-34',
                  'S20810-35': 'SAUCONY-Guide-16-muska-tenisica-S20810-35',
                  'S70665-28': 'SAUCONY-Shadow-5000-muska-tenisica-S70665-28',
                  'S70773-1': 'SAUCONY-Grid-Shadow-2-unisex-tenisica-S70773-1',
                  'S70773-2': 'SAUCONY-Grid-Shadow-2-unisex-tenisica-S70773-2',
                  'S70773-3': 'SAUCONY-Grid-Shadow-2-unisex-tenisica-S70773-3',
                  'S70775-2': 'SAUCONY-Shadow-5000-unisex-tenisica-S70775-2',
                  'S70781-1': 'SAUCONY-Shadow-6000-unisex-tenisica-S70781-1',
                  'S70782-1': 'SAUCONY-Grid-Shadow-2-unisex-tenisica-S70782-1',
                  'S70786-3': 'SAUCONY-Shadow-6000-Gtx-muska-tenisica-S70786-3',
                  'S70790-1': 'SAUCONY-Jazz-Nxt-unisex-tenisica-S70790-1',
                  'S70790-3': 'SAUCONY-Jazz-Nxt-unisex-tenisica-S70790-3',
                  'SAU900016-IDA3': 'SAUCONY-Saucony-String-Bag-torba-SAU900016-IDA3',
                  'SA81153-ZST': 'SAUCONY-Freedom-Short-Sleeve-m-t-maja-SA81153-ZST',
                  'SA81181-BKBK': 'SAUCONY-Run-Lux-Short-m-kr-hlace-SA81181-BKBK',
                  'SA81538-VR': 'SAUCONY-Hydralite-Short-Sleeve-z-t-maja-SA81538-VR',
                  'SAM800058-DGH': 'SAUCONY-Mens-Life-On-The-Run-Cdwn-Jgr-m-hlace-SAM800058-DGH',
                  'SAW800105-HTG': 'SAUCONY-Wmns-Life-On-The-Run-Cdwn-Ls-z-maja-SAW800105-HTG',
                  'SA81538-VS': 'SAUCONY-Hydralite-Short-Sleeve-z-t-maja-SA81538-VS'}

picture_folder_path = './src/resize'

for sku, model in sku_model_dict.items():

    model_folder_path = os.path.join(picture_folder_path, model)
    if not os.path.exists(model_folder_path):
        os.makedirs(model_folder_path)

    sku_picture_files = [f for f in os.listdir(
        picture_folder_path) if f.startswith(sku)]

    for picture_file in sku_picture_files:
        picture_file_path = os.path.join(picture_folder_path, picture_file)
        shutil.move(picture_file_path, model_folder_path)
