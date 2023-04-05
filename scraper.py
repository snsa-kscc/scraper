import requests
import time

urls = ['S10370-5', 'S10373-8', 'S10387-5', 'S10410-2', 'S10413-2', 'S10413-35', 'S10415-30', 'S10415-35', 'S10423-2', 'S10423-30', 'S10449-35', 'S20355-7', 'S20373-30', 'S20392-9', 'S20410-2', 'S20410-35', 'S20411-35', 'S20415-30', 'S20423-30', 'S20444-35',
        'S29032-2', 'S60368-2', 'S60368-44', 'S60405-10', 'S60419-1', 'S60419-2', 'S70368-19', 'S70368-21', 'S70368-34', 'S70368-4', 'S70369-4', 'S70400-1', 'S70416-2', 'S70416-3', 'S70424-1', 'S70424-3', 'SA81165-VRR', 'SA81173-BK', 'SA81173-CR', 'SA81676-BK', 'SA81676-BT']

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
