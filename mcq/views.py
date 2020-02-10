from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.forms.models import model_to_dict

from .models import *
import random

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    context = {}

    # get all module id list from module table, and shuffle to get an id
    module = Module.objects.all()
    module_id = []

    moduleId = list(Module.objects.all().values('id'))
    for v in moduleId:
        module_id.append(v['id'])
    random.shuffle(module_id)
    first_module_id = module_id[0]
    context["module"] = module.get(id=first_module_id)

    # use module id to retrieve all relevant questions from questions table, and shuffle
    questions = list(Question.objects.filter(module_under_id=first_module_id))
    random.shuffle(questions)
    context["question"] = questions

    # get the choice based on question id
    question_choice = []
    question_id = []
    for i in questions:
        question_id.append(i.id)

    for i in question_id:
        question_choice.append(list(Choice.objects.filter(question_under_id=i)))

    context['choice'] = question_choice

    highestScore = Score.objects.all()

    context['highestScore'] = highestScore

    return HttpResponse(template.render(context, request))

# def submit_result(request):
