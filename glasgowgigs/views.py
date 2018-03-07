from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    return render(request, 'glasgowgigs/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'glasgowgigs/about.html', context=context_dict)
