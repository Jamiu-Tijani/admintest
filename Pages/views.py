from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import date
from .models import user_create
from django.core.mail import send_mail
from Test.settings import EMAIL_HOST_USER

# Create your views here.
def welcome(request):
    context = {

    }
    
    return render(request, 'welcome.html', context)
def home(request):
    
    return render(request, 'index.html')

def process(request):
    username = request.POST.__getitem__("username")
    password = request.POST.__getitem__("pass")
    mail = request.POST.__getitem__("mail")
    user_create.objects.create(username= username, password = password, is_superuser= True, date_joined=date.today().strftime('%Y-%m-%d') , email=mail)
    user_create.save
    context = {
        'message' : "user created"
    }
    return render(request, 'success.html', context )

def sendmail(request):
    print(User.objects.order_by('date_joined'))
    context = {
        #'mailinglist' : user_create.objects.all().
    }
    return render(request, 'mail.html', context)

# def send(request):

def send(request):
    def get_mails(mails):
        mail_list = []
        for mail in mails:
            if '@' in mail:
                mail_list.append(mail)
        return mail_list
    mailing_list = get_mails(User.objects.all().values_list('email', flat = True))
    mail = request.POST.__getitem__("mail")
    send_mail('Automated mail',mail,EMAIL_HOST_USER , mailing_list, fail_silently=False)
    context = {
        'message' : 'sent'
    }
    return render(request, "sent.html", context)