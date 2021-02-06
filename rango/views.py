from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.ojects.orderby('-likes')[:5]
    context_dict['boldmessage'] = 'Crunchy, creamy. cookie, candy, cupcake!'
    context_dict ['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)
    


# Create your views here.
