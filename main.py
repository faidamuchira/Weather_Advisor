import random
from datetime import datetime
import requests

def get_weather(city):
    API_KEY = "a3d5fc96ad4e09e9136a368f75bb1cb6"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    condition = data["weather"][0]["main"]
    
    return temperature, condition

# This function analyzes temperature and weather condition n returns advice for the user
def give_advice(temp, condition):

# Convert condition to lowercase to avoid case-sensitivity issues
    condition = condition.lower()

# Check temperature ranges and return appropriate advice
    if temp < 0:
        return "❄️ Freezing weather! Wear heavy warm clothes and stay indoors if possible."

    elif temp < 10:
        if condition == "rainy":
            return "🌧️ Cold and rainy — wear a coat and take an umbrella."
        return "🧥 It's cold — wear a warm coat."

    elif temp < 20:
        if condition == "rainy":
            return "🌦️ Mild but rainy — bring a light jacket and umbrella."
        return "🙂 Mild weather — a light jacket is perfect."

    elif temp < 30:
        if condition == "clear":
            return "☀️ Warm and sunny — great day for light clothes and outdoor activities!"
        return "🌤️ Warm weather — wear light clothes and stay comfortable."

    else:
        return "🔥 Very hot! Stay hydrated, wear light clothes, and avoid too much sun."
  
# This function generates a random activity suggestion based on temperature and weather condition  
def get_random_suggestion(temp, condition):

# Check weather condition and temperature to decide suitable activities
    if condition.lower() == "rainy":
        suggestions = [
            "Stay indoors and watch a movie 🎬",
            "Read a book 📚",
            "Try cooking something new 🍳"
        ]

    elif temp < 10:
        suggestions = [
            "Stay warm with a hot drink ☕",
            "Wear cozy clothes and relax 🛋️",
            "Do some indoor exercise 🧘"
        ]

    elif temp > 25:
        suggestions = [
            "Go for a walk 🚶",
            "Hang out with friends 🌞",
            "Go for a swim 🏊"
        ]

    else:
        suggestions = [
            "Go for a walk 🚶",
            "Visit a café ☕",
            "Do something productive 💻"
        ]

    return random.choice(suggestions)

# Saves weather data to a text file in a structured format.
# Includes city, temperature, condition, advice, suggestion,
# and timestamp for each entry.
def save_to_file(city, temp, condition, advice, suggestion):
    with open("weather_report.txt", "a", encoding="utf-8")as file:
        file.write("\n-------------------------------\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write(f"City: {city.title()}\n")
        file.write(f"Temperature: {temp}°C\n")
        file.write(f"Condition: {condition.title()}\n")
        file.write(f"Advice: {advice}\n")
        file.write(f"Suggestion: {suggestion}\n")
        file.write("-------------------------------\n")

while True:
    # Ask user for input
    city = input("Please enter the name of the city: ").strip()
    
    temperature, condition = get_weather(city)

    # Display weather info
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")

    # Get advice
    advice = give_advice(temperature, condition)
    print(f"Advice: {advice}")

    # Get suggestion
    suggestion = get_random_suggestion(temperature, condition)
    print(f"Suggestion: {suggestion}")
    
    # Save file
    save_to_file(city, temperature, condition, advice, suggestion)

    # Ask user to continue
    choice = input("\nWould you like to check another city? (Y/N): ").strip().upper()
    if choice == "N":
        print("Goodbye 👋")
        break

        

        

    
    
    

