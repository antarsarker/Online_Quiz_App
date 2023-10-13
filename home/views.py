from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *
import random

# Create your views here.

def home(request):
    return render(request ,'home.html')

def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:

            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
                
            })
        
        payload = {'status' : True , 'data' : data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")
