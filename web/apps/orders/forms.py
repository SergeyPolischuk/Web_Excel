from django import forms
from .models import *

class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        # fields = []     #поля, которые необходимо включить
        exclude = ['']    #поля, которые необходимо исключить
