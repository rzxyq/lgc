from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.core.mail import send_mail

def arrayToText(array):
    str = ""
    for x in array:
        str = str + x + ", "
    print(str)
    return str[0:-2]

def basic(request):
    """ Homepage """
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            netid = (form.cleaned_data['netid']).strip()
            if NewStudent.objects.filter(netid=netid).count() > 0:
                return HttpResponseRedirect('/error_exists/')
            hometown = form.cleaned_data['hometown']
            year = form.cleaned_data['year']
            school = form.cleaned_data['school']
            major = form.cleaned_data['major']
            minor = form.cleaned_data['minor']
            extracurriculars = form.cleaned_data['extracurriculars']
            extra_sa = form.cleaned_data['extra_sa']
            if extra_sa == '':
                extra_sa = "None"
            career = form.cleaned_data['career']
            career_sa = form.cleaned_data['career_sa']
            if career_sa == '':
                career_sa = "None"
            print(career_sa)
            sa1 = form.cleaned_data['sa1']
            sa2 = form.cleaned_data['sa2']
            sa3 = form.cleaned_data['sa3']
            survey = form.cleaned_data['survey']
            student = NewStudent(name = name,
                    netid = netid,
                    hometown = hometown,
                    year = year,
                    college = school,
                    major = major,
                    minor = minor,
                    extracurricular = arrayToText(extracurriculars),
                    extra_sa = extra_sa,
                    career = arrayToText(career),
                    career_sa = career_sa,
                    sa1 = sa1,
                    sa2 = sa2,
                    sa3 = sa3)
            student.save()
            mail_title = 'Let\'s Get Coffee: Thanks!'
            message = 'Thank you for taking the time to sign up as a new student for the Fall 2015 Round of Let\'s Get Coffee. We are thrilled to have you participating in this initiative.\n\nAfter the survey window has closed on Saturday, September 12, we will share your survey responses with upperclassmen in your college and major, providing them with the opportunity to handpick you based on similar interests. Then, it is their responsibility to email you to arrange a meeting at a public places on campus. We will let you know once you have been selected by an upperclassman via email.\n\nPlease let us know if you have any questions or concerns. \n\nThanks, \nThe Let\'s Get Coffee Steering Committee'
            email = 'Let\'s Get Coffee<letsgetcoffeecornell@gmail.com>'
            recipients = [student.netid + '@cornell.edu']
            send_mail(mail_title, message, email, recipients)
            return HttpResponseRedirect('/thanks_newstudent/')
    else:
        form = NewStudentForm()
    return render(request, 'newstudent/basic.html', {
        'form' : form,
        'request' : request, })

#For closed state
def newstudent_closed(request):
    return render(request, 'newstudent_closed.html', {
        'request' : request, })
