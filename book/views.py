from django.shortcuts import render, redirect
from book.models import Book
from book.forms import BookForm

def main(request):
    books = Book.objects.order_by('-created_at')

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # reload page
    else:
        form = BookForm()

    return render(request, 'main.html', {'form': form, 'books': books})
