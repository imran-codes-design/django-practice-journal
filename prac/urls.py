from django.urls import path
from .views import my_view
urlpatterns = [
    path('user/',my_view)
]
