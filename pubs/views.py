from django.shortcuts import render
from django.core.mail import send_mail
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from pubs.models import Book, Publication

# Create your views here.
def index(request):
	publication_list = Publication.objects.all().order_by('-year')
	#output = ', '.join([p.headline for p in publication_list])
	template = loader.get_template('pubs/index.html')
	context = RequestContext(request, {'publication_list': publication_list,
	})
	return HttpResponse(template.render(context))

def search_form(request):
	return render(request, 'books/search_form.html')

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'publications/search_result.html',{'books':books,'query':q})
	return render(request, 'publications/search_form.html', {'error': error})

def contact(request):
	errors = []
	if request.method == 'POST':	
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid email address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email','NoEmailEntered@sunnyrock.info'),
				['li_rockman@hotmail.com'],
			)
			return HttpResponseRedirect('thanks/')
	return render(request, 'books/contact_form.html', {
		'errors': errors,
		'subject': request.POST.get('subject', ''),
		'message': request.POST.get('message', ''),
		'email': request.POST.get('email', ''),
	})
def thanks(request):
	return HttpResponse('Thank you for your input!')
