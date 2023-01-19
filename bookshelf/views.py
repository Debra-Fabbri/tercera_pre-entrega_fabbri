from django.views.generic import (CreateView, DetailView, ListView, TemplateView,
                                  UpdateView)

from .forms import AuthorForm, BookForm, BookFormEdit
from .models import Author, Book
from django.forms.widgets import HiddenInput

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'my-author-create.html'
    form_class = AuthorForm
    success_url = '/my-books'

class BooksView(ListView):
    model = Book
    template_name = 'my-books.html'


class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'
    
    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    #form_class = BookFormEdit;
    #fields = ['title','author','anio_pub']
    fields = []
    success_url = '/my-books'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.append('title')
        self.fields.append ('author')
        self.fields.append('anio_pub')
        # add your own logic
        #self.form_class.esconde_campo(True);
        #self.fields['title'].widget = HiddenInput()

class BookCreateView(CreateView):
    model = Book
    template_name = 'my-book-create.html'
    form_class = BookForm
    success_url = '/my-books'
    
