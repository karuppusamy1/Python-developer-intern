<<<<<<< HEAD
# chatapp/views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from json.decoder import JSONDecodeError
import json
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

@csrf_exempt
@require_http_methods(["POST", "OPTIONS", "GET"])
def getchatresponse(request):
    if request.method == "POST" and request.body:
        try:
            data = json.loads(request.body)
            chat_prompt = data.get("prompt", "").lower()

            if chat_prompt:
                
                api_key ='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'

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                }
                api_endpoint ="https://api.openai.com/v1/completions"

                openai_data = {
                    "model": "text-davinci-003",
                    "prompt":chat_prompt,
                    "max_tokens": 200,
                    "temperature": 0
                }

                     # Make the actual request to the OpenAI API
                response = requests.post(api_endpoint, headers=headers, json=openai_data)
   
            if response.ok:
                json_data = response.json()
                response_text = json_data['choices'][0]['text']
                return JsonResponse({"response":response_text})
            else:
                print('OpenAI API Error:', response.status_code, response.reason)
                err = response.text
                print('Error details:', err)
            return JsonResponse({"error": err}, status=response.status_code)
        except JSONDecodeError:
          return JsonResponse({"error": "Invalid JSON in the request body"}, status=400)
    return JsonResponse({"error":"Invalid request method or empty body"},status=400)

def index(request):
    return render(request,'index.html')



def favicon(request):
    # You can replace 'path_to_your_favicon.ico' with the actual path to your favicon
    favicon_data = open('path_to_your_favicon.ico', 'rb').read()
    return HttpResponse(favicon_data, content_type='image/x-icon')

def home(request):
=======
# chatapp/views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from json.decoder import JSONDecodeError
import json
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

@csrf_exempt
@require_http_methods(["POST", "OPTIONS", "GET"])
def getchatresponse(request):
    if request.method == "POST" and request.body:
        try:
            data = json.loads(request.body)
            chat_prompt = data.get("prompt", "").lower()

            if chat_prompt:
                
                api_key ='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'

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                }
                api_endpoint ="https://api.openai.com/v1/completions"

                openai_data = {
                    "model": "text-davinci-003",
                    "prompt":chat_prompt,
                    "max_tokens": 200,
                    "temperature": 0
                }

                     # Make the actual request to the OpenAI API
                response = requests.post(api_endpoint, headers=headers, json=openai_data)
   
            if response.ok:
                json_data = response.json()
                response_text = json_data['choices'][0]['text']
                return JsonResponse({"response":response_text})
            else:
                print('OpenAI API Error:', response.status_code, response.reason)
                err = response.text
                print('Error details:', err)
            return JsonResponse({"error": err}, status=response.status_code)
        except JSONDecodeError:
          return JsonResponse({"error": "Invalid JSON in the request body"}, status=400)
    return JsonResponse({"error":"Invalid request method or empty body"},status=400)

def index(request):
    return render(request,'index.html')



def favicon(request):
    # You can replace 'path_to_your_favicon.ico' with the actual path to your favicon
    favicon_data = open('path_to_your_favicon.ico', 'rb').read()
    return HttpResponse(favicon_data, content_type='image/x-icon')

def home(request):
>>>>>>> c757b4711a9f228aefeee01ee108df6d6dddfde9
    return render(request,'home.html')