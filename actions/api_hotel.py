import requests

def book_hotel(city_name,country_name):
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    querystring = {"cityName":city_name,"countryName":country_name}

    headers = {
        'x-rapidapi-host': "best-booking-com-hotel.p.rapidapi.com",
        'x-rapidapi-key': "api key provided by rapidapi"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.json())
    print(city_name)
    print(country_name)
    print(response.json())
    return response.json()

book_hotel("London","United Kingdom")