from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Retrieve all books written by a specific author."""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def get_books_in_library(library_name):
    """Retrieve all books available in a specific library."""
    Library.objects.get(name=library_name)
    return Library.books.all()

def get_librarian_of_library(library_name):
    """Retrieve the librarian of a specific library."""
    librarians = Librarian.objects.get(library__name=library_name)
    return librarians