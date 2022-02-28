from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject = name + " : "+subject,
            body = message,
            to = ['faustinofilipe6@gmail.com'],
            headers = {"Reply.To": email}
        )
        email_message.send()
        messages.success(request,f'Obrigado,,,ita nia mensajen haruka ona ho susesu!!!')
    return render(request,'base/home.html')