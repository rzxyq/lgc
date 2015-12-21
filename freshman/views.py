from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.core.mail import send_mail

def fresh(request):
    """ Homepage """
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            netid = (form.cleaned_data['netid']).strip()
            student = NewStudent(name = name,
                    netid = netid,
                    )
            student.save()
            return HttpResponseRedirect('/')
    else:
        form = NewStudentForm()
    return render(request, 'freshman.html', {
        'form' : form,
        'request' : request, })
