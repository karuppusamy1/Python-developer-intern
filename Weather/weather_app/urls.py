from django.urls import path
from .views import weather, weather_alert, home


urlpatterns = [
    path('weather/', weather, name='weather'),
    path('weather_alert/', weather_alert, name='weather_alert'),
    path('', home,name='home'),
]

