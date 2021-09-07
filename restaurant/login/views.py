from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.



#login View
def user_login(request):
  if request.method == 'POST':
    fm = AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
      uname = fm.cleaned_data['username']
      upass = fm.cleaned_data['password']
      user = authenticate(username=uname,password=upass)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
        #messages.success(request,"Login successful")
        

  else:
    fm = AuthenticationForm()
  return render(request,"login/login.html",{"form":fm})
  


def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')