# Crypto Project

This project demonstrates the use of Object-Oriented Programming (OOP) principles and APIs in Python. It fetches cryptocurrency data from the CoinGecko API and displays it in a user-friendly format.

When prompted, enter the cryptocurrency ID (e.g., "bitcoin", "ethereum","Tether", "Solana") to fetch its data.

This example project demonstrates the use of OOP principles and interaction with a public API to fetch cryptocurrency data. 

The README file provides clear instructions for setting up and using the project.

## import requests

This line imports the requests library, which is used to make HTTP requests to APIs

## class Crypto:
    def __init__(self, id, symbol, name, price_usd):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.price_usd = price_usd

    def __str__(self):
        return f"{self.name} ({self.symbol}): ${self.price_usd:.2f}"
The Crypto class represents a cryptocurrency.
The __init__ method initializes the class with the following attributes:
id: The unique identifier of the cryptocurrency (e.g., bitcoin).
symbol: The symbol of the cryptocurrency (e.g., btc).
name: The name of the cryptocurrency (e.g., Bitcoin).
price_usd: The current price of the cryptocurrency in USD.
The __str__ method returns a formatted string representation of the Crypto object.

## class CryptoAPI:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
The CryptoAPI class is responsible for interacting with the CoinGecko API.
The __init__ method sets the base URL for the CoinGecko API.

## def get_crypto_price(self, crypto_id):
        endpoint = f"{self.base_url}/simple/price"
        params = {
            'ids': crypto_id,
            'vs_currencies': 'usd'
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return data[crypto_id]['usd']
The get_crypto_price method retrieves the current price of a cryptocurrency.
It constructs the URL for the API request, sets the parameters (crypto_id and the currency usd), and makes a GET request.
The response.raise_for_status() line ensures that an HTTPError is raised for unsuccessful requests (e.g., 404 or 500 errors).
The response is parsed as JSON and the USD price of the cryptocurrency is returned.

## def get_crypto_details(self, crypto_id):
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
The get_crypto_details method retrieves detailed information about a cryptocurrency.
It constructs the URL for the API request and makes a GET request.
The response is parsed as JSON, and a Crypto object is created with the details retrieved from the API.
The Crypto object is then returned.

## def main():
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
The main function is the entry point of the script.
It creates an instance of the CryptoAPI class.
It prompts the user to enter the cryptocurrency ID (e.g., bitcoin or ethereum) and converts the input to lowercase and strips any extra spaces.
It tries to get the details of the cryptocurrency using the get_crypto_details method of the CryptoAPI class.
If successful, it prints the details of the cryptocurrency.
If an HTTP error or any other error occurs, it prints an appropriate error message.

