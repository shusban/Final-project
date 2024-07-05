# This line imports the requests library, which is used to make HTTP requests to APIs

import requests

class Crypto:
    def __init__(self, id, symbol, name, price_usd):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.price_usd = price_usd

    def __str__(self):
        return f"{self.name} ({self.symbol}): ${self.price_usd:.2f}"

class CryptoAPI:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_crypto_price(self, crypto_id):
        endpoint = f"{self.base_url}/simple/price"
        params = {
            'ids': crypto_id,
            'vs_currencies': 'usd'
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return data[crypto_id]['usd']

    def get_crypto_details(self, crypto_id):
        endpoint = f"{self.base_url}/coins/{crypto_id}"
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        crypto = Crypto(
            id=data['id'],
            symbol=data['symbol'],
            name=data['name'],
            price_usd=self.get_crypto_price(crypto_id)
        )
        return crypto

def main():
    crypto_api = CryptoAPI()

    crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").strip().lower()
    try:
        crypto = crypto_api.get_crypto_details(crypto_id)
        print(crypto)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    main()
