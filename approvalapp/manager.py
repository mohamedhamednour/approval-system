from django.db import models
from django.db.models import Count, F, Q



class ApprovalQuerySet(models.QuerySet):

    def with_total_counts(self):
         return self.aggregate(
            total_pending=Count('id', filter=Q(status='Pending')),
            total_approved=Count('id', filter=Q(status='Approved')),
            total_rejected=Count('id', filter=Q(status='Rejected')),
        )
