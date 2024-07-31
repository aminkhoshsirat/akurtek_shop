from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', AccountView.as_view(), name='index'),
]