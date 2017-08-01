from django.contrib import admin

from .models import (
    Author,
    Book,
    BookCopy,
    Category,
    Publisher
)

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(BookCopy)