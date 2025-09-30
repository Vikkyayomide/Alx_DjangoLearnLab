from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
        related_name= 'books'
    )
    
    def __str__(self):
        return self.title
    

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(
        Book,
        related_name= 'libraries'
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
CHOICES = (
    ('admin', 'Admin'),
    ('member', 'Member'),
    ('Librarian', 'Librarian'),
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=CHOICES, default='member')
    def __str__(self):
        return f"{self.user.username} - {self.role}"