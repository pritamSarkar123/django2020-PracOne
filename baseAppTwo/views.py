from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'baseAppTwo/index.html', {'comment': 'hello world pritam', 'value': 100, 'name': 'my name is pritam sarkar'})


def other(request):
    return render(request, 'baseAppTwo/other.html')


def relative(request):
    return render(request, 'baseAppTwo/relative.html')
