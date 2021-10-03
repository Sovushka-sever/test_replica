from django.db import models


class Worker(models.Model):
    """
    Модель сотрудник.
    """

    fio = models.CharField(
        verbose_name='Имя сотрудника',
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'
        db_table = 'worker'
