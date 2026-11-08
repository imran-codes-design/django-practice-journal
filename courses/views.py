from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    student={
        'name':"ali",
        'course':'Django',
        'duration':'3 months',
        'instructor': 'Muhammad Imran',
        'courses': ['Python', 'Django', 'React', 'Machine Learning']
    }
    return render(request,'courses/home.html',student)
def course_list(request):
    return HttpResponse("This is the Course List Page")


def course_detail(request):
    return HttpResponse("This is the Course Detail Page")


def about(request):
    return HttpResponse("About Our Course Management System")


def contact(request):
    return HttpResponse("Contact Us")
# Create your views here.
def course_detail_by_id(request,id):
    return HttpResponse(f"{id}")
def course_details_by_name(request,name):
    return HttpResponse(f"{name}")