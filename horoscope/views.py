from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_info_about_sign_zodiac(request, sign_zodiac):
    return HttpResponse('Это знак зодиака')

def leo(request):
    return HttpResponse('Это знак зодиака лев')