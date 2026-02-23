from django.shortcuts import render
from django.http import HttpResponse
 
def members(request):
    return HttpResponse("Hello world Everyone, SF241, welcome to the members page of my tennis club!")