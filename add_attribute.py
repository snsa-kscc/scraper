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
    'options': ['SAUMFTW']
}

product_skus = ['S70671-3', 'S2108-828', 'S2108-826', 'S2044-667', 'S70674-2', 'S70665-2', 'S70665-13',
                'S70665-11', 'S70665-6', 'S2044-654', 'S70404-49', 'S70613-13', 'S2044-648', 'S70539-20', 'S70665-1', 'S70404-50']


for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    existing_attributes.append(new_attribute)
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    print(wc_api.put(f"products/{product_id}", payload))
