import requests
def currency(your_country,new_country,amount):
    # your_country = input('Enter any country: ')
    # new_country = input('Enter any country: ')
    # amount = input('Enter your amount: ')
    api = 'your api key'


    country_api_url = f'https://api.api-ninjas.com/v1/country?name={your_country}'
    country_response = requests.get(country_api_url, headers={'X-Api-Key': api })
    if country_response.status_code == requests.codes.ok:
        my_currency_code = country_response.json()[0]['currency']['code']

    country_api_url2 = f'https://api.api-ninjas.com/v1/country?name={new_country}'
    country_response2 = requests.get(country_api_url2, headers={'X-Api-Key': api })
    if country_response2.status_code == requests.codes.ok:
        new_currency_code = country_response2.json()[0]['currency']['code']  

    currency_api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={new_currency_code}&have={my_currency_code}&amount={amount}'
    currency_response = requests.get(currency_api_url, headers={'X-Api-Key': api})
    if currency_response.status_code == requests.codes.ok:
        new_amount = currency_response.json()['new_amount']
        new_currency = currency_response.json()['new_currency']
        old_currency = currency_response.json()['old_currency']
        old_amount = currency_response.json()['old_amount']
        data = f'{old_amount} {old_currency} is equivalent to {new_amount} {new_currency}'
        return data

# response =currency('Bangladesh','India','100')

# print(response)