from django.shortcuts import render
from .models import Book

def list_books(request):
    """
    A function-based view that:
    - pulls every Book from the database
    - hands them to a template called list_books.html
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})




from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    """
    Class-based view that:
    - Displays details for a single Library
    - Shows all books in that library
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'



from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # Redirect to a success page.
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile
from django.shortcuts import render

def is_admin(user):
    return hasattr(user, 'userprofile')and user.userprofile.role == 'admin'
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    # Your admin-specific logic here
    return render(request, 'relationship_app/admin_view.html')

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'
@login_required
@user_passes_test(is_member)
def member_view(request):
    # Your member-specific logic here
    return render(request, 'relationship_app/member_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    # Your librarian-specific logic here
    return render(request, 'relationship_app/librarian_view.html')