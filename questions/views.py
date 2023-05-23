from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from questions.models import Questions 
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
    question = Questions.objects.get(id = id)
    question.search_count = question.search_count + 1
    question.save()
    
    template = loader.get_template('questions/try.html')
    context = {
        'result': '', 
        'question' : question,
    }
    return HttpResponse(template.render(context, request))

def get_by_id(request, id):
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
    file = open('scripts/user_input.py','w')
    file.writelines(data)
    file.close()

def execute(request):
    input_text = request.POST.get('user_input')
    # Encode the input as bytes
    input_bytes = input_text.encode()

    result = subprocess.run(['python', 'scripts/user_input.py'], input=input_bytes, capture_output=True,  )

    if result.returncode == 0:
        output = result.stdout.decode()
    else:
        output = result.stderr.decode("utf-8")
    return "<pre>{}</pre>".format(output)

def search(request):
    query = request.GET.get('q')
    results = Questions.objects.filter(title__icontains=query)[:10]
    data = [{'id': r.id, 'title': r.title, 'description': r.description} for r in results]
    return JsonResponse({'results': data})

def top_search():
    query = request.GET.get('q')
    results = Questions.objects.filter(title__icontains=query)
    data = [{'id': r.id, 'title': r.title, 'description': r.description} for r in results]
    return JsonResponse({'results': data})