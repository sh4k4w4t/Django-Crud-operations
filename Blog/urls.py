from django.urls import path
from Blog.views import index,book_list

app_name = 'Blog'

urlpatterns = [
    path('', index,name='index'),
    path('books/<int:author_id>/', book_list,name='books'),
]