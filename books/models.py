from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    adress = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title




