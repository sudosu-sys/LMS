from django.urls import path
from lms.views import book_list

urlpatterns = [
    path('', book_list, name='book_list'),
]
