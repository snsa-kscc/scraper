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

modified_attribute = {'id': 2,
                      'options': ['Saucony Originals']
                      }

product_skus = ['S70463-6', 'S70512-2', 'S70512-3',
                'S60368-128', 'S60368-160', 'S70404-32', 'S60405-38']
for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    for attribute in existing_attributes:
        if attribute['id'] == modified_attribute['id']:
            attribute.update(modified_attribute)
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    wc_api.put(f"products/{product_id}", payload).json()
