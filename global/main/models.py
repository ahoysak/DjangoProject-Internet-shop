from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Device(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=20, default='2022')
    country = models.CharField(max_length=100)
    camera = models.CharField(max_length=10)
    dynamic = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.CharField(max_length=100, default='100$')
    link = models.TextField(default='/')
    type_device = models.CharField(max_length=255, default='Смартфон')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default='Samsung')


    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Пристрій'
        verbose_name_plural = 'Пристрої'


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


