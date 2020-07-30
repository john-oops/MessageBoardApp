from django.db import models


# Create your models here.
class Post(models.Model):  # создание модели бд с текстом
    text = models.TextField()

    def __str__(self):
        '''
        строковое отображение модели
        :return:
        '''
        return self.text[:50]
