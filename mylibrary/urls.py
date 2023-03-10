from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views import generic
from django.shortcuts import redirect

# Para retornar imágenes estáticas
from django.conf import settings
from django.conf.urls.static import static

# Para retornar media en modo insecure
from django.views.static import serve

from bookshelf import views
from bookshelf import old_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', views.WelcomeView.as_view()),
    url(r'^my-books/', views.BooksView.as_view()),
    url(r'^book-detail-by-id/(?P<pk>[-\w]+)',
        views.BookDetailByIdView.as_view()),
    url(r'^book-detail-by-code/(?P<code>[-\w]+)',
        views.BookDetailByCodeView.as_view()),
    url(r'^book-update/(?P<pk>[-\w]+)$', views.BookUpdateView.as_view()),
    url(r'^book-create$', views.BookCreateView.as_view()), 
    url(r'^author-create$', views.AuthorCreateView.as_view()),   

    url(r'^old/welcome/', old_views.welcome),
    url(r'^old/my-books/', old_views.get_books_list),
    url(r'^old/book-detail-by-id/(?P<pk>[-\w]+)',
        old_views.get_book_by_id),
    url(r'^old/book-detail-by-code/(?P<code>[-\w]+)',
        old_views.get_book_by_code),
    url(r'^old/book-update/(?P<pk>[-\w]+)',
        old_views.edit_book),
    url(r'^documentacion/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
