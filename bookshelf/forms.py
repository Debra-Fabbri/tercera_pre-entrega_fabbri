from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from .models import Author, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'code', 'author',"origen_disponible", "anio_pub"]
    def esconde_campo(self,visibilidad:bool):
        self.fields['title'].widget = self.HiddenInput()
        return


    
class BookFormEdit(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'code', 'author',"origen_disponible", "anio_pub"]
    def __init__(self, *args, **kwargs):
        
        hide_condition = kwargs.pop('hide_condition',None)
        super(BookFormEdit, self).__init__(*args, **kwargs)
        self.fields['title'].widget = HiddenInput()