from django.urls import path
from . import views
app_name='courses'
urlpatterns = [
    path('',views.home),
    path('list',views.course_list),
    path('details',views.course_detail),
    path('about',views.about),
    path('contact',views.contact),
    path('<int:id>/',views.course_detail_by_id),
    path('<str:name>/',views.course_details_by_name),
]
