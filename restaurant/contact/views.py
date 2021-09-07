from django.shortcuts import render, redirect
from . forms import ContactForm
from . models import Feedback
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def send_success(request):
    return HttpResponse("Thank You")

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            # try:
            #     send_mail(subject,message,from_email,[from_email])
            # except BadHeaderError:
            #     return HttpResponse("Invalid Header")
            # return redirect('contact:send_success')
            reg = Feedback(subject=subject,message=message,from_email=from_email)
            reg.save()

    else:
        form = ContactForm()
    context = {
        'form':form
    }
    return render(request,"contact/contact.html",context)

