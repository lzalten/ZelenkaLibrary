from django.urls import path, include
from website.views import HomePageView, SignUpView, MyBooks, AddBook, LibraryView, SingleBook, LogoutView, SearchBooks, \
    DeleteBook

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('library/', LibraryView.as_view(), name='library'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    #path('search_books/', LibraryView.as_view(), name='search_books'),
    path('search_books/<str:keyword>', SearchBooks.as_view(), name='search_books'),
    path('delete_book/<int:book_id>', DeleteBook.as_view(), name='delete_book'),
    path('my_books/', MyBooks.as_view(), name='my_books'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('single_book/<int:book_id>', SingleBook.as_view(), name='single_book'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls'), name='auth')
]