from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #başka bir modele referans tanımlar.
    title = models.CharField(max_length=200) #belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
    text = models.TextField() #bu da uzun metinleri tanımlar.
    created_date = models.DateTimeField(
            default=timezone.now) #bu da gün ve saati tanımlamada kullanılır.
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title