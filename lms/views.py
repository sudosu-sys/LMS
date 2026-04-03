from django.shortcuts import render

from lms.models import Book

# Create your views here.
def book_list(request):

    all_books = Book.objects.all() # 500,000 books

    context = {
        'books': all_books,
    }
    
    return render(request, 'lms/book_list.html', context)