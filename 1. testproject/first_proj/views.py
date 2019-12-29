from django.shortcuts import render
from django.http import HttpResponse
from first_proj.models import Webpage, AccessRecord

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    accessrecord_dict = {'access_record': webpage_list}
    my_dict={'insert_me': 'This is from first_proj > views.py'}
    return render(request,'first_proj/index.html',context=accessrecord_dict)
