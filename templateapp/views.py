from django.http import request
from django.shortcuts import render, resolve_url

# Create your views here.
def index (request):
  val = 'Goodbye'
  return render(request, 'index.html', context={'value':val})

def home (request):
  my_name = 'Taro Yamada'
  favorite_fruits = ['Apple','Grape','Lemon']
  my_info = {
    'name':'Taro',
    'age': 18
  }
  return render(request, 'home.html', context = {
    'my_name' : my_name,
    'favorite_fruits' : favorite_fruits,
    'my_info' : my_info
  })

def sample1(request):
  return render(request, 'sample1.html')

def sample2(request):
  return render(request, 'sample2.html')