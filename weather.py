import requests

api_key = "ENTER_YOUR_API_KEY_HERE"
waqi_token = "ENTER_YOUR_WAQI_TOKEN_HERE"
base_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
geo_url = "https://api.openweathermap.org/geo/1.0/direct"

while True:
    city = input("\nEnter city name (or 'q' to quit): ").strip()

    if city.lower() == "q":
        print("Exiting weather app. Goodbye!")
        break

    if not city:
        continue

    # --- Current Weather ---
    params = {"q": city, "appid": api_key, "units": "metric"}
    weather_response = requests.get(base_url, params=params)
    weather_data = weather_response.json()

    if weather_response.status_code == 200:
        city_name = weather_data["name"]
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print("\n--- Current Weather ---")
        print(f"City: {city_name}")
        print(f"Temperature: {temp}°C")
        print(f"Conditions: {description}")
    else:
        print(
            f"\nError {weather_response.status_code}: {weather_data.get('message', 'Failed to fetch weather data')}"
        )
        continue

    # --- 3-Hour Forecast ---
    forecast_response = requests.get(forecast_url, params=params)
    forecast_data = forecast_response.json()

    if forecast_response.status_code == 200:
        print("\n--- 3-Hour Forecast ---")
        for forecast in forecast_data["list"][:5]:
            raw_datetime = forecast["dt_txt"]
            date_part, time_part = raw_datetime.split(" ")
            year, month, day = date_part.split("-")

            clean_date = f"{day}/{month}/{year[-2:]}"
            clean_time = time_part[:5]

            temp = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(
                f"Date: {clean_date}   Time: {clean_time}   Temp: {temp}°C   | {description}"
            )
    else:
        print(
            f"\nError {forecast_response.status_code}: Failed to fetch forecast data"
        )

# --- Air Quality Index ---
    import requests.utils

    encoded_city = requests.utils.quote(city)
    waqi_url = f"https://api.waqi.info/feed/{encoded_city}/"
    waqi_params = {"token": waqi_token}

    waqi_response = requests.get(waqi_url, params=waqi_params)
    waqi_data = waqi_response.json()

    print("--- Debug: WAQI Data ---")
    print(waqi_data)

    if waqi_response.status_code == 200 and waqi_data.get("status") == "ok":
        aqi = waqi_data["data"]["aqi"]
        station_name = waqi_data["data"]["city"]["name"]

        print("\n--- Air Quality ---")
        print(f"Station: {station_name}")
        print(f"Air Quality Index (AQI): {aqi}")
    else:
        error_message = waqi_data.get("data", "Failed to fetch Air Quality data")
        print(f"\nWAQI Error: {error_message}")