from django.contrib import admin
from .models import Skill,Project
from .models import ContactMessage
from .models import Book
admin.site.register(Skill)
admin.site.register(Project)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display= ('title','author')