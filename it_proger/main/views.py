from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<H5> Hello every one </H5>')

def about(request):
    return HttpResponse('<H4> inspect </H4>')

def resume(request):
    return HttpResponse('<H4> resume </H4>')
