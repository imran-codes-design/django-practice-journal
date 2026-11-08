from django.shortcuts import render
from django.http import HttpResponse
def my_view(request):
    context={
        'name':'imran',
        'marks':1056
    }
    
    return render(request,'core/home.html',context)