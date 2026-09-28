# Atmospheria
-------------
A Python terminal application delivering real-time weather conditions, 3-hour forecasts, and live Air Quality Index (AQI) data for cities worldwide.

---

## Features
-----------
- **Live Weather Updates:** Current temperature, humidity, and weather conditions.
- **Short-Term Forecast:** Upcoming 3-hour forecast summary.
- **Air Quality Index (AQI):** Real-time air pollution levels and health warnings.
- **Global Lookup:** Search data for any city worldwide.

---

## Prerequisites
- Python 3.8 or higher
- `requests` library

Install dependencies:
```
pip install requests
```
API Keys Setup
--------------
This project requires two free API keys:

OpenWeatherMap API Key:

-Sign up at OpenWeatherMap.
-Generate your free API key from your account dashboard.

WAQI (World Air Quality Index) Token:
-Request a free API token at WAQI API Platform.

Configuration & Usage
Open the project script (weather.py or your main Python file).

Locate the key variables and replace the placeholder text with your actual tokens:
`WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"`
`WAQI_TOKEN = "YOUR_WAQI_TOKEN"`

Run the application
------------------
python weather.py

Enter any city name when prompted, or enter q to exit.

License
-------
Distributed under the MIT License. See LICENSE for more information.
