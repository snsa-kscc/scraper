import requests
import time

# urls = ['S70424-8',
#         'S70368-203',
#         'SAU800034-BK',
#         'S10654-66',
#         'S20672-1',
#         'S10723-16',
#         'S70613-13',
#         'S10729-125',
#         'S20687-84',
#         'SAW800408-SD',
#         'SAW800412-SD',
#         'SAW800417-SD',
#         'S10729-30',
#         'S10813-10',
#         'S10813-65',
#         'S10838-25',
#         'S20775-25',
#         'S10720-86',
#         'SAM800313-UB',
#         'SAM800315-UB',
#         'SAM800316-UB',
#         'SAM800317-UB',
#         'SAM800320-UB',
#         'SAW800407-UB',
#         'SAW800408-UB',
#         'SAW800409-UB',
#         'SAW800410-UB',
#         'SAW800412-UB',
#         'SAW800413-UB',
#         'SAW800417-UB',
#         'S10838-30',
#         'S10838-75',
#         'S20838-30',
#         'S10823-36',
#         'S10823-60',
#         'S10830-30',
#         'S10881-32',
#         'S20755-75',
#         'S20813-22',
#         'S20823-33',
#         'S20830-32',
#         'S20881-21',
#         'S20881-60',
#         'S20810-34',
#         'S20810-35',
#         'S70665-28',
#         'S70773-1',
#         'S70773-2',
#         'S70773-3',
#         'S70775-2',
#         'S70781-1',
#         'S70782-1',
#         'S70786-3',
#         'S70790-1',
#         'S70790-3',
#         'SAU900016-IDA3',
#         'SA81153-ZST',
#         'SA81181-BKBK',
#         'SA81538-VR',
#         'SAM800058-DGH',
#         'SAW800105-HTG',
#         'JAZZ DOUBLE HL',  # fail
#         'SK261010',  # fail
#         'SA81538-VS',
#         '368322002',  # fail
#         '368322001',  # fail
#         '6498273',  # fail
#         '3MD30111504',  # fail
#         '6198084',  # fail
#         'UQ3800g',  # fail
#         'UA5041e',  # fail
#         'UA5052e',  # fail
#         'UQ5360g',  # fail
#         'UA5690e']  # fail

urls = ['S20756-35',
        'S20838-85',
        'S20756-25',
        'S20755-35',
        'S20755-25',
        'S10756-16',
        'BS3166',
        'BS2045 D',
        'BS2045 C',
        'BS2045 B',
        'BS2045 A',
        'BS2002 C',
        'BS3151A',
        'S20762-30',
        'SAW800253-LPRA',
        'S10392-4',
        '001509-723',
        '91662-20 - 051']

for url in urls:
    for part in range(1, 6):
        response = requests.get(
            f'https://s7d4.scene7.com/is/image/WolverineWorldWide/{url}_{part}?wid=1000&hei=1000&resMode=bilin&op_usm=1.0,1.0,8,0&iccEmbed=0&printRes=72')
        filename = f'{url}_{part}.jpg'
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {filename}.')
        else:
            print(
                f'Error {response.status_code}: Failed to download {filename}.')
        time.sleep(2)

print('Done.')
