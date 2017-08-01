from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Publisher(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=1000)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    category = models.ForeignKey(Category)
    isbn = models.BigIntegerField(unique=True)
    total_number_of_copies = models.IntegerField()
    available_number_of_copies = models.IntegerField()
    is_textbook = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BookCopy(models.Model):
    book = models.ForeignKey(Book)
    copy_number = models.IntegerField()

    def __str__(self):
        return str(self.copy_number) + " " + str(self.book)
    
    class Meta:
        verbose_name_plural = "BookCopies"