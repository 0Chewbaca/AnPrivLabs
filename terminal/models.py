from django.db import models
from django import forms
from django.utils import timezone

from django.utils import timezone

class Terminal(models.Model):
    vulnerability = models.CharField(max_length=50, default="", verbose_name="Type of Vulnerability")
    ram = models.IntegerField(null=True, default="1024", verbose_name="Amount of Ram")
    core = models.IntegerField(null=True, default="2",verbose_name="Cpu Core")


    def __str__(self):
        return self.vulnerability
 