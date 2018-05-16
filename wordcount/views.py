from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	print(fulltext)
	characters = len(fulltext)
	wordlist = fulltext.split()
	count = len(wordlist)
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1

	print(worddictionary)
	return render(request, 'count.html', {'fulltext': fulltext, 'characters': characters, 'count': count, 'worddictionary': worddictionary.items()})

def about(request):
	return render(request, 'about.html')

def dog(request):
	return HttpResponse("<h1>DAISY</h1><p>Daisy is the best little doggie!</p>")