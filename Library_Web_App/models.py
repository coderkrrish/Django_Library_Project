from django.db import models

# Create your models here.

class Book(models.Model):
    Book_Name = models.CharField(max_length=150)
    Book_Price = models.FloatField()
    Book_Author = models.CharField(max_length=100)
    Book_Genere = models.CharField(max_length=50, null=True)
    Is_Published = models.BooleanField(default = False)
    Is_Active = models.BooleanField(default = True)

    def __str__(self):
        return self.Book_Name


    class Meta:
        db_table = "Book"


class Product(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Is_Digital = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Product"
