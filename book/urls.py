from django.urls import path
from book.views import home, store_book, show_books
urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name='storebook'),
    path('show_books/', show_books, name='show_books'),
]
