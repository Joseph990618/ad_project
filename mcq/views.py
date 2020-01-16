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

    # get module id list from module table, and shuffle to get an id
    module = Module.objects.all()
    module_id = []

    moduleId = list(Module.objects.all().values('id'))
    for v in moduleId:
        module_id.append(v['id'])
    random.shuffle(module_id)
    first_module_id = module_id[0]
    context["module"] = module.get(id=first_module_id)

    # use module id to retrieve all the questions from questions table
    question = list(Question.objects.all().filter(module_under_id=first_module_id))
    random.shuffle(question)
    context["question"] = question

    # get the choice based on question id
    

    return HttpResponse(template.render(context, request))
