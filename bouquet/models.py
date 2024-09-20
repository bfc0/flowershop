from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False,
                             null=False, verbose_name="Название")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return str(self.title)


class Budget(models.Model):
    amount = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Бюджет")

    class Meta:
        verbose_name = "Бюджет"
        verbose_name_plural = "Бюджеты"

    def __str__(self):
        return self.amount


class Bouquet(models.Model):

    title = models.CharField(max_length=100, blank=False,
                             null=False, verbose_name="Название")
    price = models.DecimalField(
        blank=False, null=False, max_digits=8, decimal_places=2, verbose_name="Цена")
    description = models.TextField(
        blank=False, null=False, verbose_name="Описание")
    composition = models.TextField(
        blank=False, null=False, verbose_name="Состав")
    image = models.ImageField(upload_to="images/")
    size = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Размер")
    events = models.ManyToManyField(Event, blank=True)

    class Meta:
        verbose_name = "Букет"
        verbose_name_plural = "Букеты"

    @property
    def formatted_price(self):
        if self.price % 1 == 0:
            return int(self.price)
        return self.price

    def __str__(self):
        return str(self.title)


class Consultation(models.Model):
    client_name = models.CharField(max_length=100,verbose_name="Имя клиента")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    registration_time = models.DateTimeField(default=timezone.now(),
                                             verbose_name="Время регистрации", blank=True, null=True)
    order_accepted = models.BooleanField(default=False, verbose_name="Заказ принят", blank=True, null=True)

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"

    def __str__(self):
        return f"{self.client_name} - {self.phone_number}"

