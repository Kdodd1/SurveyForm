from django.shortcuts import render, HttpResponse, redirect 

def index(request):

	return render(request, 'myapps/index.html')

def process(request):

	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	print('*'*90)
	print(request.session['name'])
	print('*'*90)
	return redirect('/result')

def result(request):

	return render(request, 'myapps/submitInfo.html')