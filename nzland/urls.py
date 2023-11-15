from nzland.views import *
from django.urls import path
app_name='some'
urlpatterns=[
    path('williumson/',williumson,name='williumson'),
    path('rachinravindra/',rachinravindra,name='rachinravindra'),
]