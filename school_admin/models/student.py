from django.db import models
from .lesson import ExtraLesson

class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="П.І.Б. учня")
    age = models.PositiveIntegerField(verbose_name="Вік")
    school_class = models.CharField(max_length=20, verbose_name="Клас")
    lesson = models.ForeignKey(
        ExtraLesson, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Додаткове заняття"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Учень"
        verbose_name_plural = "Учні"