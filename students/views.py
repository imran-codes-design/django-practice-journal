from django.http import HttpResponse
from django.shortcuts import render
def home(request):
     if request.method == 'POST':
       student={
           'name':request.POST.get("student_name"),
           'email':request.POST.get("email"),
           'age':request.POST.get("age"),
           'department':request.POST.get("department")
       }
       return render(request,'students/success.html',{'student':student})
    
     return render(request,'students/register.html')

# Create your views here.
