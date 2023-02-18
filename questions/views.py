from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import subprocess
import os

# Create your views here.
def index(request):
    # Store input numbers
    import datetime
    now = datetime.datetime.now()
    result = now.strftime("%Y-%m-%d %H:%M:%S")
    template = loader.get_template('index.html')
    context = {
        'result': '',
    }
    return HttpResponse(template.render(context, request))

def create(request):
    write_file(request.POST.get('text',''))
    output = result()

    template = loader.get_template('index.html')
    context = {
        'result': output,
        'text': request.POST.get('text',''),
        'user_input': request.POST.get('user_input',''),
    }
    return HttpResponse(template.render(context, request))

def write_file(data):
    file = open('scripts/user_input.py','w')
    file.writelines(data)
    file.close()

def result():
    result = subprocess.run(['python', 'scripts/user_input.py'], capture_output=True)

    if result.returncode == 0:
        output = result.stdout.decode("utf-8")
    else:
        output = result.stderr.decode("utf-8")
    return output.split('\n')