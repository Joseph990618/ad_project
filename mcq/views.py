from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.

def index(request):
    # create a emtpy varable to store the module id for avoiding same id in the next shuffle
    # get module id list from module table
    # shuffle the list
    # get the first module id in the list
    # store the module id in the previous varable
    # use module id to retrieve all the questions from questions table
    # shuffle the question list and get the first 10 questions from the list
    # try to pass to the index.html (still need to figure out the method)

    moduleList = Module.objects.all()

    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))