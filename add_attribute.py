import os
from woocommerce import API
from dotenv import load_dotenv

load_dotenv()

woocommerce_url = os.getenv('URL')
woocommerce_key = os.getenv('KEY')
woocommerce_secret = os.getenv('SECRET')

wc_api = API(
    url=woocommerce_url,
    consumer_key=woocommerce_key,
    consumer_secret=woocommerce_secret,
    version='wc/v3'
)

# new_attribute = {
#     'id': 7,
#     'name': 'sizechart',
#     'position': 5,
#     'visible': True,
#     'variation': False,
#     'options': ['ONMFTW']
# }

new_attribute = {
    'id': 3,
    'name': 'Podloga',
    'position': 3,
    'visible': True,
    'variation': False,
    'options': ['Cesta']
}

product_skus = [
    'S70790-3',
    'S70790-1',
    'S70786-3',
    'S70782-1',
    'S70773-3',
    'S70773-2',
    'S70773-1',
    'S70665-28',
    'S70754-2',
    'S70700-1',
    'S70665-3',
    'S70665-14',
    'S60690-2',
    'S60690-1',
    'S60530-21',
    'S1044-668',
    'S70742-1',
    'S70637-6',
    'S70637-5',
    'S70747-3',
    'S70528-12',
    'S70528-11',
    'S70665-24',
    'S60530-31',
    'S70671-3',
    'S2108-828',
    'S2108-826',
    'S70745-3',
    'S70744-7',
    'S70718-3',
    'S2044-657',
    'S1044-664',
    'S70539-62',
    'S70539-61',
    'S2044-665',
    'S2044-667',
    'S1044-673',
    'S1044-672',
    'S1044-670',
    'S2044-580',
    'S70368-200',
    'S70635-1',
    'S70745-1',
    'S70744-3',
    'S70674-4',
    'S70674-2',
    'S70639-2',
    'S70665-2',
    'S70665-13',
    'S70665-11',
    'S1108-829',
    'S70665-12',
    'S60530-15',
    'S2108-827',
    'S70665-6',
    'S70718-2',
    'S70639-3',
    'S60578-1',
    'S2044-654',
    'S70404-49',
    'S60530-13',
    'S60530-12',
    'S1108-801',
    'S1108-765',
    'S70404-46',
    'S70613-13',
    'S2044-648',
    'S70539-20',
    'S60539-18',
    'S2044-623',
    'S1044-626',
    'S70714-2',
    'S70643-1',
    'S70639-1',
    'S70665-1',
    'S60688-2',
    'S70587-2'
]

for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    existing_attributes.append(new_attribute)
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    print(wc_api.put(f"products/{product_id}", payload))
