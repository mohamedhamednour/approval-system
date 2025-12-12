from django.db import models
from django.conf import settings
from .conf import TYPE_CHOICES


class Company(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='users_companies'
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    company_details = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name} ({self.type})"


# Multi-table inheritance

class SmallBusiness(Company):
    number_of_employees = models.PositiveIntegerField(null=True, blank=True)
    annual_revenue = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )

class Startup(Company):
    founders = models.TextField(null=True, blank=True)
    funding_stage = models.CharField(max_length=50, null=True, blank=True)

class Corporate(Company):
    departments = models.JSONField(null=True, blank=True)
    global_branches = models.PositiveIntegerField(null=True, blank=True)



#Optional NoSQL Approach

#The project is designed to work with Django 5, which allows flexibility in database choice
# An alternative implementation can use NoSQL databases MongoDB 