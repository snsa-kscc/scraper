import requests
import time

urls = ['Z43203_44',
        'Z43202_31',
        'Z43201_77',
        'Z43201_34',
        'Z43201_09',
        'Z43104_74',
        'Z43104_07',
        'Z43102_11',
        'Z43102_07',
        'Z43101_74',
        'Z43101_70',
        'Z43101_08',
        'Z43101_07',
        'Z43101_01']

for url in urls:
    response = requests.get(
        f'https://sun68.com/media/catalog/product/Z/4/{url}.jpg')
    filename = f'{url}.jpg'
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename}.')
    else:
        print(
            f'Error {response.status_code}: Failed to download {filename}.')
    time.sleep(2)
    for char in 'BCD':
        response = requests.get(
            f'https://sun68.com/media/catalog/product/Z/4/{url}_{char}.jpg')
        filename = f'{url}_{char}.jpg'
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {filename}.')
        else:
            print(
                f'Error {response.status_code}: Failed to download {filename}.')
        time.sleep(2)

print('Done.')
