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
        'result': result,
         
    }
    return HttpResponse(template.render(context, request))

def create(request):
    write_file(request.POST.get('text',''))
    
    output = result()
    

    template = loader.get_template('index.html')
    # output = output.replace('\n', "<br/>")
    context = {
        'result': output,
        'text': request.POST.get('text','')
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
        #output = subprocess.getoutput()

    output = output.split('\n')
    return output