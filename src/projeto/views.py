from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	
	#return HttpResponse("<h1>Hello World</h1>")

	#usando shortcuts
	return render(request, "index.html", {})

def sobre_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "sobre.html", {})

def depoimentos_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "depoimentos.html", {})

def promocoes_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "promocoes.html", {})

def contato_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "contato.html", {})
