from india.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shami/',shami,name='shami'),
]