import json
import urllib.parse
import urllib.request

def get_weather(city):
    api_key = '9473a9bfc41ed54eb3c9f02af04de636'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        response = urllib.request.urlopen(url)
        data = json.load(response)
        if data['cod'] == 200:
            return data
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None



def answer_question(city, question):
    weather_data = get_weather(city)

    if weather_data:
        if question == 'current_temperature':
            return f"The current temperature in {city} is {weather_data['main']['temp']}°C."
        elif question == 'weather_description':
            return f"The weather in {city} is {weather_data['weather'][0]['description']}."
        elif question == 'humidity':
            return f"The humidity level in {city} is {weather_data['main']['humidity']}%."
        elif question == 'wind_speed':
            return f"The wind speed in {city} is {weather_data['wind']['speed']} m/s."
        else:
            return "Sorry, I couldn't understand your question."
    else:
        return f"Sorry, I couldn't retrieve weather data for {city}."


city = 'Kyiv'
print(answer_question(city, 'current_temperature'))
print(answer_question(city, 'weather_description'))
print(answer_question(city, 'humidity'))
print(answer_question(city, 'wind_speed'))