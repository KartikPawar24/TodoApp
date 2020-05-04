from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<h1>Hello Welcome to this Todo Application</h1>")
