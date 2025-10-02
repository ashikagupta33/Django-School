import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print(f"🌤️ Weather in {city}: {res.text}")
        else:
            print("❌ Failed to get weather info.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("🌦️ Terminal Weather App")
    city = input("Enter city name: ")
    get_weather(city)
