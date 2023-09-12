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
#     'options': ['SAUWAPP']
# }

new_attribute_1 = {
    'id': 5, 'name': 'Vrsta proizvoda', 'position': 1,
    'visible': True, 'variation': False, 'options': ['Tenisice']
}

new_attribute_2 = {
    'id': 3,
    'name': 'Podloga',
    'position': 3,
    'visible': True,
    'variation': False,
    'options': ['Cesta']
}

product_skus = [
    'Z43202-31',
    'Z43201-77',
    'Z43201-34',
    'Z43201-09',
    'Z43104-74',
    'Z43104-07',
    'Z43102-11',
    'Z43102-07',
    'Z43101-74',
    'Z43101-70',
    'Z43101-08',
    'Z43101-07',
    'Z43101-01']

for product_sku in product_skus:
    product = wc_api.get('products', params={'sku': product_sku}).json()[0]
    existing_attributes = product["attributes"]
    existing_attributes.extend([new_attribute_1, new_attribute_2])
    product_id = product['id']
    payload = {"attributes": existing_attributes}
    print(wc_api.put(f"products/{product_id}", payload))
