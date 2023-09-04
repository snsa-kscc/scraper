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

new_attribute = {
    'id': 7,
    'name': 'sizechart',
    'position': 5,
    'visible': True,
    'variation': False,
    'options': ['SAUWAPP']
}

product_skus = ['SA81484-BK', 'SA81538-VCT',
                'SA81750-MLT', 'SA81750-RWP', 'SAW800283-RED']
for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    existing_attributes.append(new_attribute)
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    wc_api.put(f"products/{product_id}", payload).json()
