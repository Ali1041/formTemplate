from django.urls import path
from .views import *

app_name = 'application'

urlpatterns = [
    path('',form,name='form'),
    path('payment/',payment,name='form-back'),
    path('charge', charge, name="charge"),
]