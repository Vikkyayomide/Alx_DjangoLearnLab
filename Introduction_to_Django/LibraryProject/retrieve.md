# Retrieve
>>> from bookshelf.models import Book
>>> Book.objects.all()
# Output:
# <QuerySet [<Book: Book object (1)>]>
>>> b = Book.objects.first()
>>> b.title, b.author, b.publication_year
# Output:
# ('1984', 'George Orwell', 1949)
