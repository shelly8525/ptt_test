from django.shortcuts import render
from datetime import datetime
from search.models import Company1

def hello_world(request):
    return render(request,'hello_world.html', {'current_time' : datetime.now()})

def test(request):
  title = Company1.objects.all()
  return render(request,'test.html', {'title' : title})