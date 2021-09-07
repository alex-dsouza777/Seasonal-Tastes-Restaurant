from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('',views.user_profile , name='profile'),
]