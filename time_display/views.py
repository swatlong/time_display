from django.shortcuts import render
from time import gmtime, strftime


def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,"index.html", context)
    
def times(request):
    context = {
        "time": strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    }
    return render(request,"index.html", context)
    
