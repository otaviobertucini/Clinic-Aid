from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    role = models.CharField(max_length=10, blank=False, null=True)


class Person(models.Model):

    name = models.CharField(max_length=100)  # nome
    dob = models.DateField(blank=True)  # data de nascimento
    gender = models.CharField(max_length=9)  # sexo

    def __str__(self):
        return self.name


class Patient(Person):

    cpf = models.CharField(max_length=11)
    plan = models.CharField(max_length=20)  # plano de saúde
    number = models.IntegerField()
    observations = models.TextField(max_length=200)  # observações
    # TODO: consultas relacionadas


class User(Person):

    user_x = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


class Secretary(User):

    id_x = models.CharField(max_length=3)


class Doctor(User):

    crm = models.CharField(max_length=5)
    # TODO: consultas e dias relacionados






