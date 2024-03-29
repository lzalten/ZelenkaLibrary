from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import Context
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from website.models import Book, Genre


# Create your views here.


class HomePageView(View):

    def get(self, request):
        return render(request, 'home.html')


class SignUpView(CreateView):   # registration
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LibraryView(View):  # library

    def get(self, request):
        books = Book.objects.all()  # get all book
        genres = Genre.objects.all()  # get all genres
        return render(request, 'library.html', context={'books': books,
                                                        'genres': genres})


class MyBooks(LoginRequiredMixin,View):

    def get(self, request):
        books = Book.objects.filter(user=request.user)  # get all books where user == requested user
        genres = Genre.objects.all()  # get all genres
        return render(request, 'my_books.html', context={'books': books,
                                                         'genres': genres})


class AddBook(LoginRequiredMixin, View):

    def get(self, request):
        genres = Genre.objects.all()  # get all genres
        return render(request, 'add_book.html', context={'genres': genres})

    def post(self, request):
        try:  # fill book form
            name = request.POST.get('name')
            author = request.POST.get('author')
            genre = Genre.objects.get(genre_id=int(request.POST.get('genre')))
            description = request.POST.get('description')
            link = request.POST.get('link')
        except Exception as e:
            return render(request, 'add_book')
        Book.objects.create(  # create book object
            user=request.user,
            name=name,
            author=author,
            genre=genre,
            description=description,
            link=link
        )
        return redirect('my_books')


class SingleBook(View):

    def get(self, request, book_id):
        book = Book.objects.get(book_id=book_id)  # get single book object
        return render(request, 'single_book.html', context={'book': book,
                                                            'rel_books': [book]})


class SearchBooks(View):

    def get(self, request, keyword):
        books = Book.objects.filter(
            Q(name__icontains=keyword) |
            Q(author__icontains=keyword) |
            Q(genre__name__icontains=keyword)
        )
        genres = Genre.objects.all()  # get all genres
        if books is None:
            return redirect('library')
        else:
            return render(request, 'search_books.html', context={'books': books,
                                                                 'genres': genres})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')


class DeleteBook(View):

    def get(self, request, book_id):
        try:
            Book.objects.get(book_id=book_id).delete()
            return redirect('my_books')
        except:
            pass




