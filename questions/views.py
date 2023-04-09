from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from questions.models import Questions 
import subprocess
import os

# Create your views here.

def home(request):
    questions = Questions.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/base.html', context=diction)

def about(request):
    questions = Questions.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/about.html', context=diction)

def questions(request):
    questions = Questions.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/questions.html', context=diction)
   
def try_it(request, id):
    # Store input numbers
    import datetime
    now = datetime.datetime.now()
    result = now.strftime("%Y-%m-%d %H:%M:%S")
    template = loader.get_template('questions/try.html')
    context = {
        'result': 'id',
    }
    return HttpResponse(template.render(context, request))

def result(request):
    write_file(request.POST.get('text',''))
    output = execute()

    template = loader.get_template('questions/try.html')
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

def execute():
    result = subprocess.run(['python', 'scripts/user_input.py'], capture_output=True)

    if result.returncode == 0:
        output = result.stdout.decode("utf-8")
    else:
        output = result.stderr.decode("utf-8")
    return output.split('\n')