from django import forms
from .models import Author, Reading, Friend, Book

class AuthorForm(forms.ModelForm):
    # Виджет для изменения типа ввода поля
    # full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = '__all__'

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
