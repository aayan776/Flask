from flask import Flask, render_template, request
import requests #pip install it first

app = Flask(__name__)
api_key = 'ed3d0e0233321f36dc5b3b02eb12937a'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods = ['GET', 'POST'])
def home():
    weather_data = None
    error_msg = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f'{base_url}?q={city}&APPID={api_key}&units=metric'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city' : data['name'],
                    'temperature' : data['main']['temp'],
                    'description' : data['weather'][0]['description'].title(),
                    'icon' : data['weather'][0]['icon']
                }
            else:
                error_msg = 'City not found. Please try again'
        else:
            error_msg = 'Please enter a city name'
    return render_template('weather.html', weather = weather_data, error = error_msg)

if __name__ == '__main__':
    app.run(debug = True)