import requests
import pyttsx3

def main():
    city = input('Enter the name of the city: ')

    API_key = '---- your api key here ----'
    url = f'https://api.weatherapi.com/v1/current.json?key={API_key}&q={city}'

    r = requests.get(url)
    dict1 = r.json()

    temperature = dict1['current']['temp_c']
    weather = dict1['current']['condition']['text']

    engine = pyttsx3.init()
    x = f'The current temperature of {city} is {temperature} and the weather is {weather}'
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    main()
