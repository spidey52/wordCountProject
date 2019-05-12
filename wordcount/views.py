from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    wordcount = len(text.split())

    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    

    return render(request, 'count.html', {'wordcount': wordcount, 'worddictionary': word_dict.items()  })