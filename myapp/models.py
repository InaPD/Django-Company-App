from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    number_of_employees = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.company_name
