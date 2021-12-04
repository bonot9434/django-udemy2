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
    'age' : 18
  }
  status = 20
  return render(request, 'home.html', context = {
    'my_name' : my_name,
    'favorite_fruits' : favorite_fruits,
    'my_info' : my_info,
    'status': status
  })

def sample1(request):
  return render(request, 'sample1.html')

def sample2(request):
  return render(request, 'sample2.html')

def sample(request):
  name = 'ichiro yamada'
  height = 175.5
  weight = 72
  bmi = weight / (height/100)**2
  page_url = 'ホームページ: https://github.com/bonot9434'
  favorite_fruits = [
    'Apple','Grape','Lemon'
  ]
  msg = """hello
  my name is
  ichiro"""
  msg2 = '1234567890'
  return render(request, 'sample.html', context={
    'name' : name,
    'bmi' : bmi,
    'page_url' : page_url,
    'fruits' : favorite_fruits,
    'msg' : msg,
    'msg2' : msg2
  })