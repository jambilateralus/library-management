from django.db import models


class BurrowedBook(models.Model):
    book_copy = models.OneToOneField('bookmanager.BookCopy')
    borrow_date = models.DateField()
    return_date = models.DateField()
    actual_return_date = models.DateField()
    burrowed_by = models.ForeignKey('membermanager.Member')
    issued_by = models.ForeignKey('membermanager.Librarian')

    def __str__(self):
        return str(self.book_copy) + " " + str(self.borrow_date)


class RequestedBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=400)
    publisher = models.CharField(max_length=200)
    requested_date = models.DateField()
    requested_by = models.ForeignKey('membermanager.Member')

    def __str__(self):
        return self.title + " written by " + self.author


class ReservedBook(models.Model):
    book = models.ForeignKey('bookmanager.Book')
    reserved_by = models.ManyToManyField('membermanager.Member')
    reserved_date = models.DateField()

    def __str__(self):
        return str(self.book)
