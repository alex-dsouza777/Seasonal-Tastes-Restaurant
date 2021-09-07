from django.shortcuts import render, HttpResponseRedirect
#from . forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


#profile view
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"userprofile/profile.html",{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


