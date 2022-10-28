from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
# def index(request):
#     return HttpResponse("voici mon premier exemple en django")
# entre votre nom
def index(request):
    context={'name':'Baya',}
    template=loader.get_template('first.html')
    return HttpResponse(template.render(context,request))
