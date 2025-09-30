from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)



from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'



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