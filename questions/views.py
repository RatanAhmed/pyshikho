from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from questions.models import Questions, Learn
from django.http import JsonResponse

import subprocess
import os
# Create your views here.

def home(request):
    questions = Questions.objects.all()
    top_searches = Questions.objects.all().order_by('-search_count')[:20]
    diction = { 
        'question_list' : questions,
        'top_searches' : top_searches
    }
    return render(request, 'questions/home.html', context=diction)

def about(request):
    questions = Questions.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/about.html', context=diction)

def learn_python(request):
    # questions = Questions.objects.order_by('-id')
    questions = Learn.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/learn.html', context=diction)
   
def questions(request):
    # questions = Questions.objects.order_by('-id')
    questions = Questions.objects.all()
    diction = { 'question_list' : questions}
    return render(request, 'questions/practice.html', context=diction)
   
def try_it(request, id):
    # Store input numbers
    question = Questions.objects.get(id = id)
    question.search_count = question.search_count + 1
    question.save()
    
    template = loader.get_template('questions/try.html')
    context = {
        'result': '', 
        'question' : question,
    }
    return HttpResponse(template.render(context, request))

def learn_by_id(request, id):
    question = Learn.objects.get(id = id)
    data = {'id': question.id, 'title': question.title, 'description': question.description}
    return JsonResponse({'result': data})

def practice_by_id(request, id):
    question = Questions.objects.get(id = id)
    data = {'id': question.id, 'title': question.title, 'description': question.description}
    return JsonResponse({'result': data})

def result(request, id):
    question = Questions.objects.get(id = id)
    write_file(request.POST.get('text',''))
    output = execute(request)
    template = loader.get_template('questions/try.html')
    context = {
        'result': output,
        'text': request.POST.get('text',''),
        'user_input': request.POST.get('user_input',''),
        'question' : question,
    }
    return HttpResponse(template.render(context, request))

def write_file(data):
    file = open('scripts/main.py','w')
    file.writelines(data)
    file.close()

def execute(request):
    input_text = request.POST.get('user_input')
    # Encode the input as bytes
    input_bytes = input_text.encode()

    result = subprocess.run(['python', 'scripts/main.py'], input=input_bytes, capture_output=True,  )

    if result.returncode == 0:
        output = result.stdout.decode()
    else:
        output = result.stderr.decode("utf-8")
    return "<pre>{}</pre>".format(output)

def search(request):
    query = request.GET.get('q')
    learns = Learn.objects.filter(title__icontains=query)[:50]
    questions = Questions.objects.filter(title__icontains=query)[:50]
    # data = [{'id': r.id, 'title': r.title, 'description': r.description} for r in questions]
    data1 = [{'id': r.id, 'title': r.title} for r in learns]
    data2 = [{'id': r.id, 'title': r.title} for r in questions]
    return JsonResponse({'results': data1+data2})

def top_search():
    query = request.GET.get('q')
    results = Questions.objects.filter(title__icontains=query)
    data = [{'id': r.id, 'title': r.title, 'description': r.description} for r in results]
    return JsonResponse({'results': data})