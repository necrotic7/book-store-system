from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from utils.forms import DeleteConfirmForm
from .forms import BookForm
from .models import Book


@login_required #登入需要
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required
def show(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    # except Exception:
    #     raise Http404

    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show.html', {'book': book})

@login_required
@permission_required('book.add_book', login_url = 'permission_denied') #參數(app名稱.動作_model名稱, "如果權限不足則...")
def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')

    return render(request, 'books/add.html', {'form': form})

@login_required
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')

    return render(request, 'books/edit.html', {'form': form})

@login_required
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功')
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})