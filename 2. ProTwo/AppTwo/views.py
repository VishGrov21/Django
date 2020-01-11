from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

# def index(request):
#     return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict={'insert_me':'Help Page!'}
    return render(request, 'AppTwo/index.html',context=my_dict)

def index(request):
    return HttpResponse('This is ProTwo')


def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user':user_list}
    return render(request, 'AppTwo/index.html', context=user_dict)
