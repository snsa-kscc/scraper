import requests
import time

urls = ['S10514-25', 'S10543-25', 'S10546-25', 'S10548-25', 'S10556-20', 'S10556-35', 'S10559-5', 'S10595-20', 'S20514-25', 'S20543-25', 'S20548-45', 'S20551-25',
        'S20551-45', 'S20553-2', 'S20579-30', 'S20579-40', 'S60368-128', 'S60368-160', 'S60405-38', 'S70404-32', 'S70463-6', 'S70512-2', 'S70512-3', 'SAM800197-BK', 'SAW800270-RED']

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
