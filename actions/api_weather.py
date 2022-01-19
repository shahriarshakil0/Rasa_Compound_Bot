import requests
def weather(city):
    API_key = "your api"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city 
    weather_data = requests.get(Final_url).json()
    
    kword={
        'main':weather_data['main'],
        'weather':weather_data['weather'],
        'wind':weather_data['wind'],
    }
    print(city)
    return kword

 
