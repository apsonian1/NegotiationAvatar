from django.db import models


class UserProfile(models.Model): # its inheriting the basic functionalites of a database

    Name = models.CharField
    Gender = models.CharField
    Experience = models.CharField
    Rating = models.SmallIntegerField


class Meta:
        abstract = True  # If you use abstract = True for the base class Django will only create a table for the classes that inherit
        # from the base class - no matter if the fields are defined in the base class or the inheriting class


class Purpose(models.Model):
    Role = models.CharField
    Context = models.CharField
    Topic = models.CharField


def publish(self):
    self.save()


def __str__(self):
    return self.Name




