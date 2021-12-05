from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'template_app'
urlpatterns = [
  path('', views.index, name='index'),
  path('/home/<first_name>/<last_name>', views.home, name='home'),
  path('/sample1', views.sample1, name='sample1'),
  path('/sample2', views.sample2, name='sample2'),
  path('/sample', views.sample, name='sample')
]