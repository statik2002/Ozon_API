from pprint import pprint
from environs import Env

from OzonApi import OzonApi

env = Env()
env.read_env()

api_key = env('API_KEY')
client_id = env('CLIENT_ID')

api = OzonApi(api_key, client_id)

pprint(api.get_all_product_list())
print('#########################')
pprint(api.get_product_info(1196983241))