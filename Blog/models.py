from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookInfo(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    topic = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.author} -> {self.name}"
