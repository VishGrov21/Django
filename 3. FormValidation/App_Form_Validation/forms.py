from django import forms
from django.core import validators
from App_Form_Validation.models import Form_Model


class FormName (forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    vemail = forms.EmailField(label='Verify Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Form_Model
        exclude = ['vemail']

    def clean(self):
        all_clean_data = super().clean()

        if all_clean_data['email'] != all_clean_data['vemail']:
            print("email: " + all_clean_data['email'].lower())
            print("vemail: " + all_clean_data['vemail'].lower())
            raise forms.ValidationError("Emails don't match !!")
