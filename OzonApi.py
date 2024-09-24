import requests


class OzonApi:

    def __init__(self, api_key: str, client_id: int) -> None:
        self.api_key = api_key
        self.client_id = client_id

    def __str__(self) -> str:
        return f'{self.client_id}'

    def get_all_product_list(self) -> list:
        """
        :return: возвращает список товаров
        """

        url = 'https://api-seller.ozon.ru/v2/product/list'

        headers = {
            'Content-Type': 'application/json',
            'Api-Key': self.api_key,
            'Client-Id': self.client_id
        }

        data = {
            "filter": {},
            "last_id": "",
            "limit": 1000
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        product_page = response.json().get('result')

        return product_page.get('items')

    def get_product_info(self, product_id: int, offer_id: str = "", sku: int = 0) -> dict:
        """
        Метод получения информации о товаре по его id, offer_id, sku
        :param product_id: Идентификатор товара.
        :param offer_id: Идентификатор товара в системе продавца — артикул. (не обязательно)
        :param sku: Идентификатор товара в системе Ozon — SKU. (не обязательно)
        :return:
        """

        url = 'https://api-seller.ozon.ru/v2/product/info'

        headers = {
            'Content-Type': 'application/json',
            'Api-Key': self.api_key,
            'Client-Id': self.client_id
        }

        data = {
            "offer_id": offer_id,
            "product_id": product_id,
            "sku": sku
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        return response.json().get('result')
