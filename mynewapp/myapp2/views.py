# myapp2/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to myapp2 home page!")

def contact(request):
    return HttpResponse("This is the contact page of myapp2!")
