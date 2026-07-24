from django import forms
from .models import ContactMessage
from .models import Book
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email','message']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'ሙሉ ስምዎን እዚህ ያስግቡ... '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'ምሳሌ: name@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 4,
                'placeholder': 'አስተያየት ወይም መልዕክትዎን እዚህ ይጻፉ ....'
            }),
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title' , 'author' , 'recommended_by']

        labels= {
            'title':'የመጽሃፉ ርዕስ',
            'author':'ደራሲ',
            'recommended_by':'የዕርስዎ ስም(ጠቋሚ)', 
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'የምጽሃፉን ርዕስ ያስገቡ '}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'የደራሲውን ስም ያስገቡ '}),
            'recommended_by': forms.TextInput(attrs={'class': 'form-control','placeholder': 'የእርስዎን ስም ያስገቡ '}),
        }