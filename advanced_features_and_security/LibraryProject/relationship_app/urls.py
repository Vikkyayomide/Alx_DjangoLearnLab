from django.urls import path
import relationship_app.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books', views.list_books, name='book_list'),
    path('library', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('member/', views.member_view, name='member_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('change_book/<int:book_id>/', views.change_book, name='change_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # New URL pattern for editing a book
]

