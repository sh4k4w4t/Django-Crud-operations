from django import forms
from Blog.models import Author,BookInfo
class AuthorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class BookRegistrationForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

