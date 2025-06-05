from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        help_text='Введите название ингредиента'
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=60,
        help_text='Введите единицу измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name
    
