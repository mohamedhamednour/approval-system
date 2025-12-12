from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from .conf import STATUS_CHOICES
from .manager import ApprovalQuerySet
class Approval(models.Model):
   

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='requested_approvals')
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_approvals')
    approved_at = models.DateTimeField(null=True, blank=True)

    objects  = ApprovalQuerySet.as_manager()

    def __str__(self):
        return f"{self.content_object} - {self.status}"
