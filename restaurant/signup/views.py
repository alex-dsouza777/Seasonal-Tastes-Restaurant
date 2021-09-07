from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.

#signup
def sign_up(request):
    if request.method == 'POST':
      fm = SignUpForm(request.POST)
      if fm.is_valid():
        fm.save()
        messages.success(request,"Account Created Successfully")
        
    else:
      fm = SignUpForm()
    return render(request,"signup/signup.html",{'form':fm})

