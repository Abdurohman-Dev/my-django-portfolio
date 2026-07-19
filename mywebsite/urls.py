from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import home,about,greet_user
urlpatterns = [
    path('admin/',admin.site.urls),
    path ('',home),
    path('about/',about),
    path('greet/<str:name>/',greet_user),
    path('projects/', views.projects_list, name='projects'),
    ]