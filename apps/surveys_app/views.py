from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to display all surveys created")

def new(request):
    return HttpResponse("placeholder for users to add a new survey")

