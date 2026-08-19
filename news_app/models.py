from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Заголовок новости", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    content = models.TextField("Описание новости")
    image_url = models.CharField("URL-адрес изображения", max_length=500)
    created_at = models.DateTimeField("Дата и время публикации", auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title


class Adv(models.Model):
    name = models.CharField("Название компании", max_length=255, default="Company name")
    image_url = models.CharField("URL-адрес", max_length=500)
    def __str__(self):
        return self.name
