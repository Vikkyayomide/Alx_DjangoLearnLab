from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required

from .models import Book, Library, UserProfile


# =========================
# Book Views
# =========================
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    return render(request, 'relationship_app/change_book.html')


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    return render(request, 'relationship_app/delete_book.html')


# =========================
# Library Detail View
# =========================
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


# =========================
# User Registration
# =========================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # Redirect to book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# =========================
# Role-Based Views
# =========================
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'


@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'


@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
