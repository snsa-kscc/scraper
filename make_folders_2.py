import os
import shutil

sku_model_dict = {'SA81484-BK': 'SAUCONY-Scoot-Capri-zenske-kratke-tajice-SA81484-BK',
                  'S10654-45': 'SAUCONY-Guide-14-zenska-tenisica-za-trcanje-S10654-45',
                  'S20654-45': 'SAUCONY-Guide-14-muska-tenisica-za-trcanje-S20654-45',
                  'S20654-55': 'SAUCONY-Guide-14-muska-tenisica-za-trcanje-S20654-55',
                  'S70532-1': 'SAUCONY-Grid-Web-unisex-tenisica-S70532-1',
                  'S70555-4': 'SAUCONY-Jazz-Court-unisex-tenisica-S70555-4',
                  'S70555-5': 'SAUCONY-Jazz-Court-unisex-tenisica-S70555-5',
                  'S10650-35': 'SAUCONY-Ride-14-zenska-tenisica-za-trcanje-S10650-35',
                  'S2108-790': 'SAUCONY-Shadow-Original-muska-tenisica-S2108-790',
                  'S10684-26': 'SAUCONY-Guide-15-zenska-tenisica-za-trcanje-S10684-26',
                  'S20723-45': 'SAUCONY-Kinvara-13-muska-tenisica-za-trcanje-S20723-45',
                  'S20678-16': 'SAUCONY-Triumph-19-muska-tenisica-za-trcanje-S20678-16',
                  'S20681-16': 'SAUCONY-Omni-20-muska-tenisica-za-trcanje-S20681-16',
                  'S20687-45': 'SAUCONY-Endorphin-Pro-2-muska-tenisica-za-trcanje-S20687-45',
                  'S20688-16': 'SAUCONY-Endorphin-Speed-2-muska-tenisica-za-trcanje-S20688-16',
                  'S20688-45': 'SAUCONY-Endorphin-Speed-2-muska-tenisica-za-trcanje-S20688-45',
                  'S20759-31': 'SAUCONY-Triumph-20-muska-tenisica-za-trcanje-S20759-31',
                  'S20813-65': 'SAUCONY-Endorphin-Shift-3-muska-tenisica-za-trcanje-S20813-65',
                  'S10737-30': 'SAUCONY-Peregrine-12-zenska-tenisica-za-trail-trcanje-S10737-30',
                  'SAW800283-RED': 'SAUCONY-Stopwatch-Short-Sleeve-zenska-majica-SAW800283-RED',
                  'SA81165-BK': 'SAUCONY-Hydralite-Short-Sleeve-muska-majica-kratki-rukav-SA81165-BK',
                  'SA81211-CRBH': 'SAUCONY-Dash-Seamless-Sportop-muska-majica-dugi-rukav-SA81211-CRBH',
                  'S10293-4': 'SAUCONY-Hurricane-ISO-2-zenska-tenisica-za-trcanje-S10293-4',
                  'SA81538-BAR': 'SAUCONY-Hydralite-Short-Sleeve-muska-majica-kratki-rukav-SA81538-BAR',
                  'SA81750-RWP': 'SAUCONY-Scoot-Crop-zenske-tajice-SA81750-RWP',
                  'SA81165-VPS': 'SAUCONY-Hydralite-Short-Sleeve-muska-majica-kratki-rukav-SA81165-VPS',
                  'SA81538-VCT': 'SAUCONY-Hydralite-Short-Sleeve-zenska-majica-SA81538-VCT',
                  'SA81750-MLT': 'SAUCONY-Scoot-Crop-zenske-tajice-SA81750-MLT',
                  'SAM800019-BKH': 'SAUCONY-Seamless-Sportop-muska-majica-dugi-rukav-SAM800019-BKH'}

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
