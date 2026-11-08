from django.urls import path
from .import views
urlpatterns = [
    path('addNumsForm/',views.addNumsForm),
    path('addNumsResult/',views.addNumsResult),
]

