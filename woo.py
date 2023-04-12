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

product_sku = 'S2044-449-1'
product = wc_api.get('products', params={'sku': product_sku}).json()[0]

print(product.get('id'))
