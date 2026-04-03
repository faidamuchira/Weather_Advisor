import random

def give_advice(temp, condition):

    condition = condition.lower()

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
    
def get_random_suggestion(temp, condition):

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
    

while True:
    # Ask user for input
    city = input("Please enter the name of the city: ").strip()
    temperature = float(input("Please enter the temperature in degrees Celsius: "))
    condition = input("Please enter the weather condition: ").strip()

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

    # Ask user to continue
    choice = input("\nWould you like to check another city? (Y/N): ").strip().upper()
    if choice == "N":
        print("Goodbye 👋")
        break

        

        

    
    
    

