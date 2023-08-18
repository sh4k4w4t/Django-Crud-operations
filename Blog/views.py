from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from Blog.models import Author, BookInfo
from Blog.forms import AuthorRegistrationForm, BookRegistrationForm


def index(request):
    author_list = Author.objects.order_by('first_name')
    dict = {"author_list": author_list}
    return render(request, "blog/index.html", context=dict)


def book_list(request, author_id):
    authorInformation = Author.objects.get(pk=author_id)
    allBooks = BookInfo.objects.filter(author=authorInformation).order_by('name')
    dict = {"author": authorInformation, "books": allBooks}
    return render(request, "blog/book_list.html", context=dict)


def author_registration_form(request):
    authorForm = AuthorRegistrationForm()
    if request.method == 'POST':
        authorForm = AuthorRegistrationForm(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return HttpResponseRedirect(reverse('Blog:index'))
    dict = {'form': authorForm}
    return render(request, 'blog/author_registration.html', context=dict)


def book_registration_form(request):
    bookForm = BookRegistrationForm()
    if request.method == 'POST':
        bookForm = BookRegistrationForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return HttpResponseRedirect(reverse('Blog:index'))
    dict = {'form': bookForm}
    return render(request, 'blog/book_registration.html', context=dict)


def update_author(request, author_id):
    authorInfo = Author.objects.get(pk=author_id)
    authorForm = AuthorRegistrationForm(instance=authorInfo)

    if request.method == 'POST':
        authorForm = AuthorRegistrationForm(request.POST, instance=authorInfo)
        if authorForm.is_valid():
            authorForm.save()
            return book_list(request, author_id)
    dict = {'form': authorForm}
    return render(request, 'blog/edit_author.html', context=dict)


def update_book(request, author_id, book_id):
    bookInfo = BookInfo.objects.get(pk=book_id)
    bookForm = BookRegistrationForm(instance=bookInfo)
    if request.method == 'POST':
        bookForm = BookRegistrationForm(request.POST, instance=bookInfo)
        if bookForm.is_valid():
            bookForm.save()
            return book_list(request, author_id)

    dict = {'form': bookForm}
    return render(request, 'blog/update_book.html', context=dict)


def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return index(request)


def delete_book(request, author_id, book_id):
    BookInfo.objects.get(pk=book_id).delete()
    return book_list(request, author_id)
