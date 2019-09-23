from django.db import models

#from negotiationavatar.avatar.models import UserProfile


class CommonFactor(models.Model):
    Strength = models.SmallIntegerField
    Weakness = models.SmallIntegerField
    Confidence = models.SmallIntegerField
    Interest = models.SmallIntegerField


class Subject(models.Model):
    Description = models.CharField
    Timeline = models.DateTimeField  # updates the time whenever its called
    Deadline = models.DateField
    Budget = models.SmallIntegerField


class DashBoard(models.Model):
    Agent = models.CharField
    Category = models.CharField


class Add(DashBoard):
    Title = models.CharField
    Detail = models.TextField


class KeyWords(models.Model):
    Positive = models.TextField
    Negative = models.TextField
    Interest = models.TextField
    Confidence = models.TextField


