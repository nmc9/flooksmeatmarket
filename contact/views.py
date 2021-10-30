import re

from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from owner.models import Owner
from django.core.validators import validate_email
from django import forms


# Create your views here.
def index(request):
    current_user = request.user
    # get Owner details to populate fields
    owner = get_object_or_404(Owner, key=0)
    context = {'user': current_user, 'owner': owner}
    return render(request, 'contact/contact.html', context)


def send(request):
    current_user = request.user
    # get Owner details to populate fields
    owner = get_object_or_404(Owner, key=0)
    context = {'user': current_user, 'owner': owner}

    if request.method == 'POST':
        toE = get_object_or_404(Owner, key=0).email
        fromE = request.POST['id_user_email']
        subject = request.POST['id_subject']
        content = request.POST['id_content']
        context['subject_post'] = subject
        context['content_post'] = content

        try:
            validate_email(fromE)
        except forms.ValidationError:
            context['error_email'] = 'Please Enter A Valid Email'
            return render(request, 'contact/contact.html', context)
        if not validation(subject):
            context['error_email'] = 'Invalid Characters in subject'
            return render(request, 'contact/contact.html', context)

        content = content + " This message went sent from the account" + current_user.username
        msg = EmailMessage(subject, content, fromE, [toE])
        msg.content_subtype = "html"
        msg.send()
    context['msg_email'] = 'Message Sent'
    context['subject_post'] = ""
    context['content_post'] = ""
    return render(request, 'contact/contact.html', context)


def validation(validation_string):
    validation_string = validation_string.replace(" ", "")
    ''' The validation pattern with a few changes is from
    http://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
    '''
    if re.match("^[A-Za-z0-9_-]*$", validation_string):
        print(validation_string)
        return True
    print(validation_string)
    return False
