from django.db.models.signals import post_save
from .models import Client , Company
from approvalapp.models import Approval
from approvalapp.conf import PENDING

def create_approval(sender, instance, created, **kwargs):
    if created:
        Approval.objects.create(
            content_object=instance,
            status=PENDING,
            requested_by=instance.user
        )

post_save.connect(create_approval, sender=Client)
post_save.connect(create_approval, sender=Company)
