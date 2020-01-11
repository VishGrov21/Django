from django.shortcuts import render
from App_Form_Validation import forms
from App_Form_Validation.models import Form_Model
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'App_Form_Validation/index.html')


def func_form_name(request):
    var_user_form = forms.FormName()

    if request.method == 'POST':
        var_user_form = forms.FormName(request.POST)

        if var_user_form.is_valid():
            print("validation success !!")
            print("Name is " + var_user_form.cleaned_data['name'])

            Form_Model_obj = Form_Model()
            Form_Model_obj.name = var_user_form.cleaned_data['name']
            Form_Model_obj.email = var_user_form.cleaned_data['email']
            Form_Model_obj.password = var_user_form.cleaned_data['password']

            Form_Model_obj.save()
            return HttpResponseRedirect('/')

    return render(request, 'App_Form_Validation/form-page.html', context={'form': var_user_form})
