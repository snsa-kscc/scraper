import requests
import time

urls = ['S1044-521', 'S2044-449', 'S2044-580', 'S20482-50', 'S60368-9',
        'S70368-10', 'S70404-10', 'S70532-1', 'S70532-2', 'S70598-1', 'S70601-1']

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
