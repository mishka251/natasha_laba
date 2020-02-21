from django.db import models


# Create your models here.

class Patient(models.Model):
    # id автоматически будет
    # фамилия
    surname = models.CharField(max_length=200)
    # имя
    name = models.CharField(max_length=200)
    # отчество
    patronymic = models.CharField(max_length=200)
    # день рождения(хранить возраст в БД - не вариант т.к. возраст меняется, а ДР - нет)
    birth_date = models.DateField()
    # примечание
    note = models.BinaryField(null=True)


class Number(models.Model):
    # id автоатически
    #дата-время
    datetime = models.DateTimeField()
    #результат
    result = models.CharField(max_length=25)
    #ссылка на видео
    citation = models.URLField()
    #прочее
    etc = models.BinaryField(null=True)
    #пациент
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, null=True)
