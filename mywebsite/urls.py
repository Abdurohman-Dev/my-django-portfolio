from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('about/', views.about , name='about'),
    path('greet/<str:name>/',views.greet_user , name='greet_user'),
    path('projects/', views.projects_list, name='projects'),
    path('contact/',views.contact_view,name='contact'),
    path('',views.home, name='home'),
    path('books/',views.Book_list_view, name='book_list'),
    path('add-book/', views.add_book_view,name='add_book'),
    path('book/<int:pk>/',views.book_detail_view, name='book_detail'),
    path('book/<int:pk>/delete/', views.delete_book_view, name='delete_book'),
   ]