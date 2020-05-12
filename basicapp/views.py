from django.shortcuts import render
from . import forms
# Create your views here.


def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            print(f'{name} {email} {text}')
    return render(request, 'basicapp/home.html', {'form': form})
