# Update
>>> b = Book.objects.first()
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
# Output:
# (no explicit output, but the title is updated)
>>> b.title
# Output:
# 'Nineteen Eighty-Four'
