import requests
import time

urls = ['S70424-8',
        'S70368-203',
        'SAU800034-BK',
        'S10654-66',
        'S20672-1',
        'S10723-16',
        'S70613-13',
        'S10729-125',
        'S20687-84',
        'SAW800408-SD',
        'SAW800412-SD',
        'SAW800417-SD',
        'S10729-30',
        'S10813-10',
        'S10813-65',
        'S10838-25',
        'S20775-25',
        'S10720-86',
        'SAM800313-UB',
        'SAM800315-UB',
        'SAM800316-UB',
        'SAM800317-UB',
        'SAM800320-UB',
        'SAW800407-UB',
        'SAW800408-UB',
        'SAW800409-UB',
        'SAW800410-UB',
        'SAW800412-UB',
        'SAW800413-UB',
        'SAW800417-UB',
        'S10838-30',
        'S10838-75',
        'S20838-30',
        'S10823-36',
        'S10823-60',
        'S10830-30',
        'S10881-32',
        'S20755-75',
        'S20813-22',
        'S20823-33',
        'S20830-32',
        'S20881-21',
        'S20881-60',
        'S20810-34',
        'S20810-35',
        'S70665-28',
        'S70773-1',
        'S70773-2',
        'S70773-3',
        'S70775-2',
        'S70781-1',
        'S70782-1',
        'S70786-3',
        'S70790-1',
        'S70790-3',
        'SAU900016-IDA3',
        'SA81153-ZST',
        'SA81181-BKBK',
        'SA81538-VR',
        'SAM800058-DGH',
        'SAW800105-HTG',
        'JAZZ DOUBLE HL',
        'SK261010',
        'SA81538-VS',
        '368322002',
        '368322001',
        '6498273',
        '3MD30111504',
        '6198084',
        'UQ3800g',
        'UA5041e',
        'UA5052e',
        'UQ5360g',
        'UA5690e']

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
