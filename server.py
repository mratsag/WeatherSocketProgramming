from flask import Flask, render_template, request
import requests  # type: ignore

app = Flask(__name__)

# Fetch weather data using OpenWeather API
def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c053c6525483b5222dbd11fd59549c04&units=metric"
    response = requests.get(url)
    return response.json()

# Parse the weather data
def parse_weather_data(weather_data):
    try:
        weather_desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']

        # Determine weather condition for CSS class
        if 'cloud' in weather_desc:
            weather_condition = 'cloudy'
        elif 'clear' in weather_desc:
            weather_condition = 'sunny'
        elif 'rain' in weather_desc:
            weather_condition = 'rainy'
        elif 'snow' in weather_desc:
            weather_condition = 'snowy'
        else:
            weather_condition = 'default'

        return {
            'description': f"Current weather: {weather_desc}, Temperature: {temp}°C",
            'condition': weather_condition
        }
    except KeyError:
        return {'description': "Failed to parse weather data.", 'condition': 'default'}

# Home route to show the form for city input
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle city input and show weather result
@app.route('/weather', methods=['POST'])
def weather():
    city_name = request.form['city_name']
    weather_data = fetch_weather_data(city_name)
    if 'main' in weather_data:
        parsed_data = parse_weather_data(weather_data)
        return render_template('result.html', 
                               weather_info=parsed_data['description'], 
                               city_name=city_name, 
                               weather_condition=parsed_data['condition'])
    else:
        error_msg = "Failed to retrieve weather data. Please try again."
        return render_template('result.html', weather_info=error_msg, city_name=city_name, weather_condition='default')

if __name__ == '__main__':
    app.run(debug=True)