from django.urls import path
from mom.views import *
app_name='momrelation'

urlpatterns=[
    path('lakshmi/',lakshmi,name='lakshmi'),
]