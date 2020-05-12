from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm


def home(request):
    return render(request, 'second_app/homeTwo.html')


def help(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            return render(request, 'second_app/help.html', {'form': form, 'error': 'Correctly signup'})
    return render(request, 'second_app/help.html', {'form': form})
