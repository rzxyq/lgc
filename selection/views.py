from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import *
from upperclassman.models import Upperclassman
from newstudent.models import NewStudent
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.mail import send_mail

# def parse(str):


def login(request):
    if request.method == 'POST':
        form = SelectionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            net = (form.cleaned_data['netid']).strip()
            try:
            	data = Upperclassman.objects.get(netid=net)
            except ObjectDoesNotExist:
            	return HttpResponseRedirect('/error_login/')
            if data.finished:
            	 return HttpResponseRedirect('/error_selected/')
            elif name == data.name:
            	selectees = NewStudent.objects.filter(Q(major=data.major1) |
            		Q(major=data.major2) | Q(major=data.major3)).filter(selected=False)
                if selectees.count() < 5:
                    selectees = NewStudent.objects.filter(college=data.college).filter(selected=False)
                if selectees.count() < 5:
                    selectees = NewStudent.objects.filter(selected=False)

                return render(request, 'selection/select.html', {
                    'request': request,
                    'user': data,
                    'students': selectees})
            else:
                return HttpResponseRedirect('/error_login/')
    else:
        form = SelectionForm()
    return render(request, 'selection/login.html', {
        'form': form,
        'request': request, })

def closed(request):
    return render(request, 'selection_closed.html', {
        'request': request, 
        })

def selection(request):
    selected_choice = request.POST['row']
    print selected_choice
    arr = selected_choice.split(',')
    upperid = arr[1]
    lowerid = arr[0]
    upper = Upperclassman.objects.get(id=upperid)
    if upper.finished:
        return HttpResponseRedirect('/error_chosen/')
    try:
    	data = NewStudent.objects.get(netid=lowerid)
    	if data.selected == True:
    		return HttpResponseRedirect('/error_taken/')
    	data.upperclassman = upper
    	data.selected = True
    	data.save()
    	upper.finished = True
    	upper.save()
    except ObjectDoesNotExist:
    	return HttpResponseRedirect('/error_DNE/')
    mail_title = 'Let\'s Get Coffee: Selection Complete!'
    message = 'Thank you for completing the selection process of Let\'s Get Coffee.\n\n' + 'You have selected ' + data.name + ' (' + data.netid + ') as your new student in the Fall 2015 Round of Let\'s Get Coffee.\n\nWe ask that you please email your new student within 48 hours to arrange a meeting at a public location on campus (The new student will receive your netid when you select them). When you email your new student, please introduce yourself as his or her new upperclassman connection via Let\'s Get Coffee.\n\nIf you have any questions, please email letsgetcoffeecornell@gmail.com. We hope you have an awesome meeting with your new student that becomes the start of a great friendship.' + '\n\nBest, \nThe Let\'s Get Coffee Steering Committee\n'
    email = 'Let\'s Get Coffee<letsgetcoffeecornell@gmail.com>'
    recipients = [upper.netid + '@cornell.edu']
    send_mail(mail_title, message, email, recipients)
    mail_title2 = 'Let\'s Get Coffee: Selection Complete!'
    message2 = 'Congratulations! You were just selected by an upperclassman participating in Let\'s Get Coffee.\n\n' + upper.name + ' (' + upper.netid + ') will serve as your upperclassman connection in the Fall 2015 Round of Let\'s Get Coffee. It is his or her responsiblity to email you to arrange a meeting at a public place on campus by the end of Monday, September 14.\n\nIf you do not hear from your upperclassman by September 14, please be patient and give them a little more time. If you do not hear from them by Wednesday, please send them an email introducing yourself as their new student connection via Let\'s Get Coffee.\n\nIf you do not hear back from them or have any other questions or concerns, please send us an email at letsgetcoffeecornell@gmail.com. We hope you have an awesome meeting with your upperclassman that becomes the start of a great friendship.' + '\n\nBest, \nThe Let\'s Get Coffee Steering Committee\n'
    email2 = 'Let\'s Get Coffee<letsgetcoffeecornell@gmail.com>'
    recipients2 = [data.netid + '@cornell.edu']
    send_mail(mail_title2, message2, email2, recipients2)
    return HttpResponseRedirect('/thanks_selection/')
