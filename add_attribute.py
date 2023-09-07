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
    'options': ['SAUMAPP']
}

product_skus = [
    'SAM800301-BKH',
    'SAM800275-BK',
    'SAM800244-LN',
    'SAM800190-BK',
    'SAM800243-BK',
    'SAM800279-LGH',
    'SAM800278-RNH',
    'SAM800278-LGH',
    'SA81165-FL',
    'SAM800277-RNH',
    'SAM800296-BK',
    'SAM800299-BK',
    'SAM800297-BK',
    'SAM800310-BK',
    'SAM800185-DGHBK',
    'SAM800273-DGH',
    'SAM800303-BKH',
    'SAM800286-BK',
    'SAM800212-SL',
    'SAM800112-LM',
    'SAM800039-DGH',
    'SA81283-VPPR',
    'SA81392-BLBVPP']

for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    existing_attributes.append(new_attribute)
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    print(wc_api.put(f"products/{product_id}", payload))
