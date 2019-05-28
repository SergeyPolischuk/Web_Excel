from django.http import HttpResponse
from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def index(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        print(form)

    return render(request, "main_page.html", locals())