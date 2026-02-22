from django.db import models

class Teacher(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    middle_name = models.CharField(max_length=100, verbose_name="По батькові")
    description = models.TextField(verbose_name="Характеристики")

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}."

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"