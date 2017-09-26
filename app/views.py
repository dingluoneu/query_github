from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def test(request):
    return HttpResponse("This is a test!")


def profile(request):
    json_list = []
    req = requests.get("https://api.github.com/users/dingluoneu")
    json_list.append(json.loads(req.text))
    parsed_data = []
    user_data = {}
    for data in json_list:
        user_data['name'] = data['name']
        user_data['blog'] = data['blog']
        user_data['email'] = data['email']
        user_data['public_gists'] = data['public_gists']
        user_data['public_repos'] = data['public_repos']
        user_data['avatar_url'] = data['avatar_url']
        user_data['followers'] = data['followers']
        user_data['following'] = data['following']
    parsed_data.append(user_data)
    return HttpResponse(parsed_data)
