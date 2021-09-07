from django.shortcuts import render,redirect
from .models import Reservation
from .forms import ReserveTableForm, DateInput, TimeInput
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            subject = ("Reservation At Plates Of Flavor")
            message = ("Your reservation has been confirmed. Thank You For Choosing Us")
            email = reserve_form.cleaned_data['email']
            try:
                send_mail(subject,message,email,[email])
                # messages.success(request,"Your Table Is Reserved")
                # return HttpResponseRedirect("/profile/")
            except BadHeaderError:
                return HttpResponse("Invalid Header")
            
    context = {'form':reserve_form}
    return render(request,'reservation/reservation.html',context)