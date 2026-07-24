from email.mime import message
from django.shortcuts import render , redirect , get_object_or_404
from .models import Skill,Project
from .forms import ContactForm , BookForm
from django.contrib import messages
from .forms import Book
def home (request):
    skills = Skill.objects.all()
    context = {
        'username': 'አብዱሮህማን ' ,
        'role': 'የወደፊቱ ባለሙያ Full-stack Developer ',
        'skills':skills
        }
    return render(request, 'home.html',context)
def about(request):
    return render (request, 'about.html')
def greet_user(request,name):
    context = {'user_name': name}
    return render(request,'greet.html',context)
def projects_list(request):
    projects = Project.objects.all()
    context = { 'projects':projects}
    return render(request,'projects.html',context)
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"አመሰግናለሁ! መልዕክትዎት በተሳካ ሁኔታ ዳታቤዝ ውስጥ ተቀምጧል፡፡")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'myapp/contact.html',{'form': form})
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'myapp/add_book.html',{'form':form})
def Book_list_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render (request,'myapp/book_list.html',context)
def book_detail_view(request, pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request,'myapp/book_detail.html', {'book': book})
def delete_book_view(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request,'myapp/delete_book_confirm.html',{'book':book})