from django.shortcuts import render
from django.http import HttpResponse
 
def members(request):
    return HttpResponse("<h2>Revilla: Hello world Everyone, SF241, welcome to the members page of my tennis club!</h2>")