from django.db import models
from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  # blank заполнение необязательно
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add добавляет время и дату добавления/создания

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'