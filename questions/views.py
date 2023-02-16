from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import subprocess

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

    result = subprocess.run(['python', 'scripts/user_input.py'], capture_output=True)
    if result.returncode == 0:
        output = result.stdout
    else:
        output = result.stderr

    template = loader.get_template('index.html')
    context = {
        'result': output
    }
    return HttpResponse(template.render(context, request))

def write_file(data):
    file = open('scripts/user_input.py','w')
    file.writelines(data)
    file.close()