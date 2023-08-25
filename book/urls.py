from django.urls import path
from book.views import home, store_book
urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name='storebook'),
]
