from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index." + "<br><br>" + '<img src="https://view.moezx.cc/images/2018/04/29/big_20180429b.jpg" alt="big_20180429b.jpg" border="0" />')