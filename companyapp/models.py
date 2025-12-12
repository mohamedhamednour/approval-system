from django.db import models
from .conf import TYPE_CHOICES
from userapp.models import User
from .manager import ClientQuerySet , CompanyQuerySet

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_companies')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    company_details =  models.JSONField(null=True, blank=True)
    # models_usecase.py Optional Approach to handle different company types
    objects = CompanyQuerySet.as_manager()


    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')
    objects = ClientQuerySet.as_manager()

    class Meta:
            unique_together = ('user', 'company')  
            
    def __str__(self):
        return self.user.username + " - " + self.company.name