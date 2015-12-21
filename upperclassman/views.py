from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import *
from models import *
from django.core.mail import send_mail

def upper(request):
	""" Homepage """
	if request.method == 'POST':
		form = UpperClassmanForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			netid = (form.cleaned_data['netid']).strip()
			if Upperclassman.objects.filter(netid=netid).count() > 0:
				return HttpResponseRedirect('/error_exists/')
			year = form.cleaned_data['year']
			school = form.cleaned_data['school']
			major1 = form.cleaned_data['major1']
			major2 = form.cleaned_data['major2']
			major3 = form.cleaned_data['major3']
			survey = form.cleaned_data['survey']
			organization = form.cleaned_data['organization']
			upperclass = Upperclassman(name=name,
				netid=netid,
				year=year,
				college=school,
				major1=major1,
				major2=major2,
				major3=major3,
				survey=survey,
				organization=organization)
			upperclass.save()
			mail_title = 'Let\'s Get Coffee: Thanks!'
			message = 'Thank you for taking the time to sign up as an upperclassman for the Fall 2015 Round of Let\'s Get Coffee. We are thrilled to have you participating in this initiative. \n\nAfter the survey window has closed on Saturday, September 12, we will share with you the survey responses of new students in your college and major, providing you with the opportunity to handpick a new student based on similar interests. Then, it is your responsibility to email them to arrange a meeting at a public place on campus. We will remind you when the selection process has begun via email.\n\nPlease let us know if you have any questions or concerns.\n\nThanks, \nThe Let\'s Get Coffee Steering Committee'
			# Thanks, \n
			# The CampusConnection Steering Committee\n\n
			# Blake Barr (bab354)\n
			# Emma Jesch (eaj54)\n
			# Jimmy Chen (jsc349)\n
			# Alice Chou (aec247)\n
			# Sofia Hu (shh83)\n
			# Yixuan Zhang (yz427)'''
			email = 'Let\'s Get Coffee<letsgetcoffeecornell@gmail.com>'
			recipients = [upperclass.netid + '@cornell.edu']
			send_mail(mail_title, message, email, recipients)
			return HttpResponseRedirect('/thanks_upperclassman/')
	else:
		form = UpperClassmanForm()
	return render(request, 'upperclassman/basic.html', {
		'form' : form,
		'request' : request, })

#For closed state
def upperclassman_closed(request):
	return render(request, 'upperclassman_closed.html', {
		'request' : request, })
