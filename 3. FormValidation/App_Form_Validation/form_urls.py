from django.urls import path
from App_Form_Validation import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-form', views.func_form_name, name="user form"),
]
