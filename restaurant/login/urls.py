from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.user_login , name='login'),
    path('log_out/',views.user_logout , name='logout'),
]
