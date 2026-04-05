# 📝 Project Title
### Weather Advisor
## 📌 Description
This project is a console-based Weather Advisor application.It allows the user to enter a city and retrieves weather data from an API. The program processes this data to provide useful advice, such as clothing suggestions and activity recommendations.The results are displayed to the user and saved to a file. The user can also check multiple cities in one session.

## ⚙️ Features
* User can enter a city name
* Retrieves real-time weather data from an API
* Provides clothing advice based on temperature
* Suggests activities based on weather conditions
* Saves results to a text file (weather_report.txt)
* Allows repeated searches using a loop
* Handles errors (invalid city, API issues, empty input)

## 🔑 API Used
This project uses the OpenWeather API:
https://openweathermap.org/api

It retrieves:
* Temperature
* Weather condition (e.g., Clear, Rainy, Cloudy)
## ⚙️ Setup Instructions
### 1. Create a virtual environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux: source venv/bin/activate
### 2. Install dependencies
pip install -r requirements.txt
### 3. Set up environment variables
Create a .env file in the project root and add:

API_KEY = api_key_here
### 4. Run the program
python main.py

## 📁 Output File
The program saves results to:

weather_report.txt

Each entry includes:
* Date
* City
* Temperature
* Weather condition
* Advice
* Activity suggestion
