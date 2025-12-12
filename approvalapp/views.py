from rest_framework import viewsets , mixins
from django.utils import timezone
from .models import Approval
from .serializers import ApprovalSerializer
from .permissions import IsSuperUser
from shared.utils import GenericResponse


class ApprovalViewSet(mixins.UpdateModelMixin,mixins.ListModelMixin , viewsets.GenericViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [IsSuperUser]


    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return GenericResponse(data=serializer.data, approval=qs.with_total_counts())


    def perform_update(self, serializer):
        serializer.save(
            approved_by=self.request.user,
            approved_at=timezone.now()
        )
