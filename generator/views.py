from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list(map(lambda x: x.upper(), characters)))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*()'))

    lenght = request.GET.get('lenght', 8)

    thepassword = ''

    for i in range(int(lenght)):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')