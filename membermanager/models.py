from django.db import models


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    registered_year = models.DateField()
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    registered_year = models.DateField()
    email_address = models.EmailField()
