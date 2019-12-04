from django.http import HttpResponse
from django.shortcuts import render
import operator

#Lets say someone wants to jump into the homepage
#Everytime someone visits the home URL the request object is being sent
#Functions can be whatever you wish for
def home(request):
    #Determines what we send back to the end-user
    #Standalone string won't work, we need to send out the HTTP response, this is where our imports come to play
    # return "hello"!
    # return HttpResponse('Hello')
    #Here we map the request to our HTML template, utilize the import to grab our render util, we can pass dict to it with some data
    return render(request, 'home.html',{'hithere' : 'This is me Mario!'})
    
    # We can toy around with some HTML straight up here, but that won't suffice in longer run
    # return HttpResponse(<h1>Our very important Header coming through!</h1>)
    # return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    #We pull out the element from our request and assign it to variable
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    variables = {
        'fulltext': fulltext,
        'count': len(wordlist),
        'worddictionary': sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    }

    return render(request, 'count.html', variables)
