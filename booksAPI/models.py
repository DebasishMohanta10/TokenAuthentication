from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField()
    category = models.ManyToManyField('Category',related_name='books')

    def __str__(self):
        return self.name




