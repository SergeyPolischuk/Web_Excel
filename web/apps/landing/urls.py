from django.urls import path
from web.apps.landing import views

urlpatterns = [
    path('', views.index, name='index')
]
