from django.db import models
from .teacher import Teacher

class ExtraLesson(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва заняття")
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE, 
        verbose_name="Викладач"
    )
    description = models.TextField(verbose_name="Опис заняття")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Додаткове заняття"
        verbose_name_plural = "Додаткові заняття"