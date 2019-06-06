from django.http import HttpResponse
from django.shortcuts import render
from ..orders.forms import OrderForm

# Create your views here.

def index(request):
    form = OrderForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # print(request.POST)
        # print(form.cleaned_data)
        # print(form.cleaned_data['customer_name'])
        form = form.save(commit=False)
        form.save()
    else:
        form = OrderForm()

    return render(request, 'landing3.html', locals())
