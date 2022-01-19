# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.events import SlotSet
from .api_weather import weather
from .api_email import send_email
from .api_currency import currency
import datetime
from .api_hotel import book_hotel
from .api_flight import get_flight

class ActionChatSummary(Action):
    '''Chat Summary'''
    def name(self) -> Text:
        return "action_chat_summary"

    async def run(
    self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        time = str(datetime.datetime.now())[:19]
        subject = f"Conversation Summary at {time}"
        conversation=tracker.events
        message=''
        for i in conversation:
            if i['event'] == 'user':
                # print('user: {}'.format(i['text']))
                message += 'user: {}\n'.format(i['text'])
        
            elif i['event'] == 'bot':
                # print('Bot: {}'.format(i['text']))
                message += 'Bot: {}\n'.format(i['text'])
        try:
            if tracker.get_slot("email_address") != None:
                send_email(tracker.get_slot("email_address"),subject,message) 
                dispatcher.utter_message(f'Chat summary is send to {tracker.get_slot("email_address")}')
        
            else:
                dispatcher.utter_message("You don't provide valid gmail address.")
        except:
            dispatcher.utter_message("Sorry, an Error occured while sending email.")
        return []


class ActionWebRtc(Action):
    '''Video Call'''
    def name(self) -> Text:
        return "action_web_rtc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = f'Video Call: "https://janus.conf.meetecho.com/videocalltest.html"'
        dispatcher.utter_message(response)

        return []

class ActionWeather(Action):
    ''' weather'''
    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            city = tracker.get_slot('location')
            temperature = round(weather(city)['main']['temp']-273.15)
            # print("this is city", city)
            desc = weather(city)['weather'][0]['description']
            hum = weather(city)['main']['humidity']
            wind_spd = weather(city)['wind']['speed']

            response = f"The current temperature at {city} is {temperature} degree Celsius. Weather is {desc}. The humidity is {hum}% and wind speed is {wind_spd}kph"
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message(
                "I can't understand your location. Please try again.")

        return [SlotSet('location', city)]


class ActionCurrency(Action):
    '''Currency'''
    def name(self) -> Text:
        return "action_currency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            my_country = tracker.get_slot("your_country")
            new_country = tracker.get_slot("new_country")
            amount = tracker.get_slot("amount")
            response =currency(my_country,new_country,amount)
        
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message("Please give me right information.")

        return [SlotSet('your_country',my_country),SlotSet('new_country',new_country),SlotSet('amount',amount)]

class ActionHotel(Action):
    '''Book Hotel'''
    def name(self) -> Text:
        return "action_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            city_name = tracker.get_slot("city_name")
            country_name = tracker.get_slot("country_name")
            data = book_hotel(city_name,country_name)
            response = f"The Hotel name is '{data['name']}'. This hotel rating is '{data['rating']}'. If you want to book this hotel please follow the link - \n'{data['link']}'"
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message("Please give me right information.")

        return [SlotSet('city_name',city_name),SlotSet('country_name',country_name)]

class ActionHotel(Action):
    '''Book Flight'''
    def name(self) -> Text:
        return "action_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            dep_city = tracker.get_slot("dep_city")
            arr_city = tracker.get_slot("arr_city")
            dep_date = tracker.get_slot("dep_date")
            data = get_flight(dep_city,arr_city,dep_date)
            # print(type(data))
            # print(data[0])
            # print(data[1])
            # print(data[2])

            # print("**********")
            # for i in data[2]:
            #     print(type(i))
            for i in data[2]['airport']:
                # print(i)
                if i['code'] == data[0]:
                    # print(i['code'])
                    departure_airport = i['name']
                    departure_city = i['city']
                    departure_country = i['country']
                    departure_location = f"Your departure location is '{departure_airport}, {departure_city},{departure_country}'."
                    # print(departure_location)

            for i in data[2]['airport']:
                # print(i)
                if i['code'] == data[1]:
                    # print(i['code'])
                    arrival_airport = i['name']
                    arrival_city = i['city']
                    arrival_country = i['country']
                    arrival_location = f"Your arrival location is '{arrival_airport}, {arrival_city},{arrival_country}'."
                    # print(arrival_location)
                    # print("\n")

            response1 = f"{departure_location}\n{arrival_location}\nHere, some flight information -\n"
            # dispatcher.utter_message("\n")
            dispatcher.utter_message(response1)
            flight_info = data[2]['airline']
            for i in flight_info[0:5]:
                try:
                    name = i['name']
                except:
                    name = "Not available"
                try:
                    book = i['checkInUrl']
                except:
                    book = "Not available"
                try:
                    phone_number = i['phoneNumber']
                    website = i['websiteUrl']
                except:
                    phone_number = "Not available"
                    website = "Not available"
                
                
                response2 = f"Airline name- '{name}';\nFor booking- '{book}';\nAny information- '{phone_number}', '{website}'\n"
                # print(response2)
                # dispatcher.utter_message("\n")
                dispatcher.utter_message(response2)

        except:
            dispatcher.utter_message("Please give me right information.")

        return [SlotSet('dep_city',dep_city),SlotSet('arr_city',arr_city),SlotSet('dep_date',dep_date)]


class ActionClear(Action):
    '''Reset All'''
    def name(self) -> Text:
        return "action_clear"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]

class ActionRestart(Action):
    '''Restart Conversation'''
    def name(self) -> Text:
      return "action_restart"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return [Restarted()]