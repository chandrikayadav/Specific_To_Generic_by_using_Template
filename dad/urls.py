from django.urls import path
from dad.views import *
app_name='dadrelation'

urlpatterns=[
    path('venkataiah/',venkataiah,name='venkataiah'),
]