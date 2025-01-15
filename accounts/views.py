from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_first(request):
  return HttpResponse("Hello!")