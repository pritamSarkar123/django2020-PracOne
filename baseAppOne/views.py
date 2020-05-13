from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'baseAppOne/index.html', {'comment': 'hello world pritam', 'value': 100, 'name': 'my name is pritam sarkar'})


def other(request):
    return render(request, 'baseAppOne/other.html')


def relative(request):
    return render(request, 'baseAppOne/relative.html')
