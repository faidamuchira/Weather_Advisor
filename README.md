# 📝 Weather Advisor
 
## 📌 Description
Weather Advisor is a console-based Python application that retrieves
real-time weather data for a user-selected city using the OpenWeather API.

The application processes the weather data and provides practical
recommendations, including clothing suggestions and activity ideas.
Users can search for multiple cities during a single session, and the
results are saved to a text file for later reference.

## ⚙️ Features
- Enter a city name and retrieve current weather information
- Retrieve real-time data from the OpenWeather API
- Provide clothing recommendations based on temperature
- Suggest activities based on weather conditions
- Save weather reports to a text file
- Search for multiple cities during a single session
- Handle invalid cities, empty input, and API errors

## 🔑 API Used
This project uses the OpenWeather API to retrieve current weather data.

The application retrieves information including:

- Temperature
- Weather conditions
- City information

API documentation: [OpenWeather API](https://openweathermap.org/api)

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/weather-advisor.git
cd weather-advisor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root and add:

```text
API_KEY=api_key_here
```

**Do not commit your `.env` file to GitHub.**

### 5. Run the program

```bash
python main.py
```

### 6. 📁 Output File

The program saves results to:

```text
weather_report.txt
```

Each entry includes:

- Date
- City
- Temperature
- Weather condition
- Advice
- Activity suggestion

### 7. 📁 Project Structure

```text
weather-advisor/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 8. 🎯 What I Learned

Through this project, I practised:

- Working with REST APIs
- Sending HTTP requests from Python
- Processing JSON responses
- Using environment variables to protect API credentials
- Handling API and user-input errors
- Working with files in Python
- Managing project dependencies
- Using Git and GitHub for version control
