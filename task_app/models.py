from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    categories = models.ManyToManyField(Category)
    descr = models.TextField()
    birth_date = models.DateField()
    experience = models.IntegerField()