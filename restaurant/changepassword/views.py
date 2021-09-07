from django.shortcuts import render, HttpResponseRedirect
#from . forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


#change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password Changed Succesfully")
                return HttpResponseRedirect("/profile/")
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,"changepassword/changepass.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


