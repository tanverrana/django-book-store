from django.urls import path
from book.views import home, store_book, show_books, edit_book
urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name='storebook'),
    path('show_books/', show_books, name='show_books'),
    path('edit_book/<int:id>', edit_book, name='edit_book'),
]
