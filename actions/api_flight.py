import requests

def get_flight(dep_city,arr_city,dep_date):
    dep_url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/locations"
    ari_url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/locations"

    dep_querystring = {"name":dep_city}
    ari_querystring = {"name":arr_city}

    headers = {
        'x-rapidapi-host': "priceline-com-provider.p.rapidapi.com",
        'x-rapidapi-key': "api key provided by rapidapi"
        }

    dep_response = requests.request("GET", dep_url, headers=headers, params=dep_querystring)
    ari_response = requests.request("GET", ari_url, headers=headers, params=ari_querystring)

    departure_airport_code = dep_response.json()[0]['id']
    print(departure_airport_code)
    # print("*********")
    arrival_airport_code = ari_response.json()[0]['id']
    print(arrival_airport_code)

    flight_url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/search"

    flight_querystring = {"location_departure":departure_airport_code,"itinerary_type":"ONE_WAY","sort_order":"PRICE","class_type":"ECO","date_departure":dep_date,"location_arrival":arrival_airport_code,"price_min":"100","price_max":"20000","duration_max":"2051"}

    flight_response = requests.request("GET", flight_url, headers=headers, params=flight_querystring)

    flight_data = flight_response.json()
    
    return departure_airport_code,arrival_airport_code,flight_data

# data = get_flight("Dhaka","Mumbai","2021-11-17")
# # print(type(data))
# # print(data[0])
# # print(data[1])
# # print(data[2])

# # print("**********")
# # for i in data[2]:
# #     print(type(i))
# for i in data[2]['airport']:
#     # print(i)
#     if i['code'] == data[0]:
#         # print(i['code'])
#         departure_airport = i['name']
#         departure_city = i['city']
#         departure_country = i['country']
#         departure_location = f"Your departure location is {departure_airport}, {departure_city},{departure_country}."
#         print(departure_location)

# for i in data[2]['airport']:
#     # print(i)
#     if i['code'] == data[1]:
#         # print(i['code'])
#         arrival_airport = i['name']
#         arrival_city = i['city']
#         arrival_country = i['country']
#         arrival_location = f"Your arrival location is {arrival_airport}, {arrival_city},{arrival_country}."
#         print(arrival_location)
#         print("\n")

# response1 = f"{departure_location}\n{arrival_location}\nHere, some flight information -\n"
# # print(response1)
# flight_info = data[2]['airline']
# for i in flight_info[0:5]:
#     try:
#         name = i['name']
#     except:
#         name = "Not available"
#     try:
#         book = i['checkInUrl']
#     except:
#         book = "Not available"
#     try:
#         phone_number = i['phoneNumber']
#         website = i['websiteUrl']
#     except:
#         phone_number = "Not available"
#         website = "Not available"
    
    
#     response2 = f"Airline name: {name}\nFor booking: {book}\nAny information: {phone_number}, {website}\n"
#     print(response2)
#     # response = response1response2
#     # return response2


# # print(data)
