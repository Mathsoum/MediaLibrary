from django.shortcuts import render

__author__ = 'Mathieu'


def index(request):
    return render(request, 'global/index.html')