import requests
import time

urls = ['S20756-35',
        'S20838-85',
        'S20756-25',
        'S20755-35',
        'S20755-25',
        'S10756-16',
        'S20762-30',
        'SAM800019-BKH',
        'SA81750-MLT',
        'SA81538-VCT',
        'SA81165-VPS',
        'SA81750-RWP',
        'SA81538-BAR',
        'S10293-4',
        'SA81211-CRBH',
        'SA81165-BK',
        'SAW800283-RED',
        'S10737-30',
        'S20813-65',
        'S20759-31',
        'S20688-45',
        'S20688-16',
        'S20687-45',
        'S20681-16',
        'S20678-16',
        'S20723-45',
        'S10684-26',
        'S2108-790',
        'S10650-35',
        'S70555-5',
        'S70555-4',
        'S70532-1',
        'S20654-55',
        'S20654-45',
        'S10654-45',
        'SA81484-BK']

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
