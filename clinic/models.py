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


class User(Person):

    user_x = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


class Secretary(User):

    id_x = models.CharField(max_length=3)


class Doctor(User):

    crm = models.CharField(max_length=5)


class Day(models.Model):

    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        # return str(self.date)
        s = str(self.date).split('-')
        return str(s[2] + '/' + s[1] + '/' + s[0])


class Time(models.Model):

    time = models.CharField(max_length=4)
    days = models.ForeignKey(Day, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.time[0:2] + ':' + self.time[2:])


class Appointment(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    secretary = models.ForeignKey(Secretary, on_delete=models.DO_NOTHING)
    reason = models.TextField(max_length=200)
    observations = models.TextField(max_length=200)
    is_return = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    date = models.ForeignKey(Day, on_delete=models.DO_NOTHING)
    date_string = models.DateField(null=True)
    hour = models.CharField(max_length=4)
    time_int = models.IntegerField(null=True)
    rapport = models.TextField(max_length=200, null=True)

    def __str__(self):
        return str(self.patient.name + ' ' + str(self.date))






