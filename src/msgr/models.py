from django.db import models


class Sms(models.Model):
    title = models.CharField('Name: ', max_length=50)
    sms = models.TextField('Option: ')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'Задача'
    #     verbose_name_plural = 'Задачи'