from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management system!")

def contact(request):
    return HttpResponse("<h2 style='color:red'> This is our contact Page </h2 >")


def show_task(request):
    return HttpResponse("welcome to our task page!")

def show_specific_task(request,id):
    print("ID: ",id)
    print("ID Type: ",type(id))
    return HttpResponse(f"Welcome to my specific task! {id}")