from django.db import models
from django.db.models import F
from django.db.models.functions import JSONObject
from django.db.models import OuterRef, Subquery
from django.contrib.postgres.fields import JSONField
from django.contrib.contenttypes.models import ContentType
from approvalapp.models import Approval


class ApprovalQuerySetMixin:
    def with_approval(self, model):
        content_type = ContentType.objects.get_for_model(model)

        approval_subquery = Approval.objects.filter(
            content_type=content_type,
            object_id=OuterRef('pk')
        ).annotate(
            approval_json=JSONObject(
                id=F('id'),
                status=F('status'),
                requested_by=F('requested_by'),
                requested_at=F('requested_at'),
                approved_by=F('approved_by'),
                approved_at=F('approved_at')
            )
        ).values('approval_json')[:1]

        return self.annotate(
            approval=Subquery(approval_subquery, output_field=JSONField())
        )


class ClientQuerySet(ApprovalQuerySetMixin, models.QuerySet):
    def info_client(self):
        from .models import Client
        return self.with_approval(Client)


class CompanyQuerySet(ApprovalQuerySetMixin, models.QuerySet):
    def info_company(self):
        from .models import Company
        return self.with_approval(Company)