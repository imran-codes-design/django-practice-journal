from django.urls import include, path
from core.views import insertForm,displayProduct
from prac.views import my_view
from django.contrib import admin  # 1. Import the admin module
from django.urls import path 

urlpatterns = [
   path("students/",include("students.urls")),
   path("courses/",include("courses.urls")),
    path("core/", include("core.urls")),
    path("",include('calculator.urls')),
    path('insertForm/',insertForm,name='insertForm'),
    path('displayProduct/' ,displayProduct,name='displayProduct'),
    path('',include('prac.urls')),
     path('admin/', admin.site.urls), 
   
   
]