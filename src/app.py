import requests

def fetch_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,windspeed_10m,relativehumidity_2m"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["current"]

def display_weather(data: dict) -> None:
    print("=" * 30)
    print("     Doha Weather — Live")
    print("=" * 30)
    print(f"  Temperature : {data['temperature_2m']} °C")
    print(f"  Humidity    : {data['relativehumidity_2m']} %")
    print(f"  Wind Speed  : {data['windspeed_10m']} km/h")
    print("=" * 30)

def main():
    DOHA_LAT = 25.2854
    DOHA_LON = 51.5310
    data = fetch_weather(DOHA_LAT, DOHA_LON)
    display_weather(data)

if __name__ == "__main__":
    main()