
#chatapp/urls.py
from django.urls import path
from . import views


app_name = "chatapp"

urlpatterns = [
    path('favicon.ico',views.favicon,name='favicon'),
    path("getchatresponse/", views.getchatresponse, name="getchatresponse"),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index')

