from django.urls import path
from Blog.views import index
from Blog.views import book_list
from Blog.views import author_registration_form
from Blog.views import book_registration_form
from Blog.views import update_author
from Blog.views import update_book
from Blog.views import delete_author
from Blog.views import delete_book

app_name = 'Blog'

urlpatterns = [
    path('', index,name='index'),
    path('books/<int:author_id>/', book_list,name='books'),
    path('author-registration/', author_registration_form,name='author_registration_form'),
    path('book-registration/', book_registration_form,name='book_registration_form'),
    path('author-update/<int:author_id>/', update_author,name='update_author'),
    path('book-update/<int:author_id>/<int:book_id>/', update_book,name='update_book'),
    path('delete-author/<int:author_id>/', delete_author,name='delete_author'),
    path('delete-book/<int:author_id>/<int:book_id>/', delete_book,name='delete_book'),
]