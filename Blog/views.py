from django.shortcuts import render
from Blog.models import Author, BookInfo


def index(request):
    author_list = Author.objects.order_by('first_name')
    dict = {"author_list": author_list}
    return render(request, "blog/index.html", context=dict)

def book_list(request,author_id):
    authorInformation= Author.objects.get(pk=author_id)
    allBooks = BookInfo.objects.filter(author= authorInformation).order_by('name')
    dict = {"author":authorInformation,"books":allBooks}
    return render(request, "blog/book_list.html",context=dict)
