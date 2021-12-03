from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'template_app'
urlpatterns = [
  path('', views.index, name='index'),
  path('/home', views.home, name='home'),
]