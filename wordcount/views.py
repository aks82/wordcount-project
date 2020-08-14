from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordlist = {}
    c=0
    for i in words:
        if i in wordlist:
            wordlist[i] +=1
        else:
            wordlist[i] = 1

    sortedlist = sorted(wordlist.items(),key=lambda x: x[1],reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(words), 'dict':sortedlist})
def about(request):
    return render(request,'about.html')