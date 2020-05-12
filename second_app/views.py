from django.shortcuts import render
from django.http import HttpResponse


def help(request):
    return render(request, 'second_app/help.html', context={'text': 'second app'})
