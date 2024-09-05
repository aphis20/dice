# myapp1/views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to myapp1!")

def about(request):
    return HttpResponse("About myapp1")

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = "Hello, world!"
    title = "Welcome to My Third Page"
    message = "This is a sample page to demonstrate passing multiple variables to a template."
    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    user = {"name": "John Doe", "age": 30}
    show_greeting = True

    mydictionary = {
        "var": var,
        "title": title,
        "message": message,
        "items": items,
        "user": user,
        "show_greeting": show_greeting
    }
    
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request,'imagepage.html')

def myform(request):
    if request.method == 'GET':
        return render(request, 'myform.html')

# If you use templates, create a `templates` directory within `myapp1`
# and render templates as follows:
# def home(request):
#     return render(request, 'myapp1/home.html')
