from django.shortcuts import render
from django.http import HttpResponse
from . models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    acc_rec = AccessRecord.objects.order_by('date')
    acc_dict = {'acc_rec': acc_rec}
    return render(request, 'first_app/index.html', context=acc_dict)
