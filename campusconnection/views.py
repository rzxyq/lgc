from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {
    'request' : request, })

def about(request):
	return render(request, 'about.html', {
		'request' : request, })

def schedule(request):
	return render(request, 'schedule.html', {
		'request' : request, })

def faq(request):
	return render(request, 'faq.html', {
		'request' : request, })

def contact(request):
	return render(request, 'contact.html', {
		'request' : request, })

def thanks_newstudent(request):
	return render(request, 'thanks_newstudent.html', {
		'request' : request, })

def thanks_upperclassman(request):
	return render(request, 'thanks_upperclassman.html', {
		'request' : request, })

def thanks_selection(request):
	return render(request, 'thanks_selection.html', {
		'request' : request, })

def error_DNE(request):
	return render(request, 'error_DNE.html', {
		'request' : request, })

def error_login(request):
	return render(request, 'error_login.html', {
		'request' : request, })

def error_taken(request):
	return render(request, 'error_taken.html', {
		'request' : request, })

def error_selected(request):
	return render(request, 'selected_already.html', {
		'request' : request, })

def error_exists(request):
	return render(request, 'error_exists.html', {
		'request' : request, })

def error_chosen(request):
	return render(request, 'error_chosen.html', {
		'request' : request, })

