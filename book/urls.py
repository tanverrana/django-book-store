from django.urls import path
# from book.views import home, store_book, show_books, edit_book, delete_book
from . import views
urlpatterns = [
    # path('', home),
    path('', views.TemplateView.as_view(template_name='home.html')),
    path('store_new_book/', views.store_book, name='storebook'),
    path('show_books/', views.show_books, name='show_books'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
]
