from django.urls import path
from .views import indexPage,insertForm,not_found


urlpatterns = [
    path('test-404/',not_found),
    path('', indexPage, name='home'),
    path('',insertForm,name='insertForm'),
   
]