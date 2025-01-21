from django.db import models
from django.core.validators import MaxLengthValidator

class Review(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Имя Клиента", null=True)
    photo = models.ImageField(upload_to='uploads/photo/', verbose_name="Фото", null=True)
    text = models.TextField(verbose_name="Текст отзыва", validators=[MaxLengthValidator(530)] )
    city = models.CharField(max_length=50, verbose_name="Город")
    created_at = models.DateField(verbose_name="Дата создания", null=True, blank=True)  # Изменили на DateField

    def __str__(self):
        return f"Отзыв от {self.customer_name}"

class Car(models.Model):
    photo = models.ImageField(upload_to='uploads/cars/', verbose_name="Фото")
    model = models.CharField(max_length=200, verbose_name="Модель машины")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (км)")
    country = models.CharField(max_length=100, verbose_name="Страна")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")


    def __str__(self):
        return f"{self.model} ({self.year})"
