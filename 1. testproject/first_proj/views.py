from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'insert_me': 'This is from first_proj > views.py'}
    return render(request,'first_proj/index.html',context=my_dict)
