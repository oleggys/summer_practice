from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):

    class Meta:
        verbose_name = 'Статья'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Заголовок', max_length=150)
    text = models.TextField('Текст статьи')
    publication_date = models.DateTimeField('', auto_now_add=True)

    def get_short_text(self):
        return self.text[:250]
