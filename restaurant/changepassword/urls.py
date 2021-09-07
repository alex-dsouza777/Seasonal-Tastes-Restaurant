from django.urls import path
from . import views

app_name = 'changepassword'

urlpatterns = [
    path('',views.user_change_pass, name='changepass'),
]
