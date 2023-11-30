# weather_app/views.py

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import WeatherAlertForm
from .forms import WeatherForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def get_weather_data(city=None, latitude=None, longitude=None):
    api_key = 'e3a8fff6b3e28b27748a318b59fa8055'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    # Determine the parameters based on the input
    params = {}
    if city:
        params['q'] = city
    elif latitude and longitude:
        params['lat'] = latitude
        params['lon'] = longitude
    else:
        return None  # If neither city nor coordinates provided, return None

    params['appid'] = api_key
    params['units'] = 'metric'  # Use 'imperial' for Fahrenheit

    # Make the API request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data =response.json()
        simplified_data = {
            'lat':weather_data['coord']['lat'],
            'lon':weather_data['coord']['lon'],
            'temp':weather_data['main']['temp'],
            'temp_min':weather_data['main']['temp_min'],
            'temp_max':weather_data['main']['temp_max'],
            'feels_like':weather_data['main']['feels_like'],
            'pressure' :weather_data['main']['pressure'],
            'humidity' :weather_data['main']['humidity'],
            'wind_speed' :weather_data['wind']['speed'],
            'weather_description' :weather_data['weather'][0]['description']
        }
        return simplified_data
     
    else:
        print('Error:', response.status_code)
        return None

@csrf_exempt
def update_weather(request):
    if request.method == 'POST' and request.is_ajax():
        city = request.POST.get('city')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        weather_data = get_weather_data(city=city, latitude=latitude, longitude=longitude)
        
        if weather_data:
            return JsonResponse({'success': True, 'weather_data': weather_data})
        else:
            return JsonResponse({'success': False, 'message': 'Error fetching weather data'})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

def weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = request.POST.get('city')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')


            if latitude and longitude:
                weather_data = get_weather_data(latitude=latitude, longitude=longitude)
            elif city:
                weather_data = get_weather_data(city=city)
            elif 'error' in weather_data:
                return render(request,'weather_app/error.html',{'error_message':weather_data['error']})
            else:
                return JsonResponse({'success': False,'message':'No valid input Provided'})
            return render(request,'weather_app/weather.html',{'weather_data': weather_data})
        else:
            return JsonResponse({'success':False,'message':'Form is not Valid'})
    else:
        form = WeatherForm()
        return render(request,'weather_app/weather_form.html', {'form' : form})
       
def weather_alert(request):
    if request.method == 'POST':
        form = WeatherAlertForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Weather Alert',
                'Significant weather change in your city. Be prepared!',
                'karuppusamykmk1@gmail.com',  # Replace with your actual email address
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('weather')
    else:
        form = WeatherAlertForm()

    return render(request,'weather_app/weather_alert.html',{'form' : form})

def home(request):
    return render(request,'weather_app/home.html')