from django.shortcuts import render

def addNumsForm(request): 
 return render(request ,'AddNumbers.html')

def addNumsResult(request):
 num1=float(request.POST['num1'])
 num2=float(request.POST['num2']) 
 res=num1+num2
 return render(request ,'AddNumbersResult.html',{'result':res})

