INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_world',
]
from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})


