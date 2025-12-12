from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Client , Company
from rest_framework import viewsets , mixins
from .serializers import ClientSerializer , CompanySerializer  
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from shared.utils import GenericResponse   

class ClientViewSet( mixins.CreateModelMixin ,mixins.ListModelMixin ,  viewsets.GenericViewSet):
    queryset = Client.objects.all().select_related('user' , 'company')
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    
    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = ClientSerializer(qs, many=True)
        return GenericResponse(data=serializer.data ,approval=qs.info_client().values_list('approval', flat=True))
    
    def get_queryset(self):
            qs = super().get_queryset().filter(user=self.request.user)
            return qs




class CompanyViewSet(mixins.CreateModelMixin ,mixins.ListModelMixin ,  viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
            qs = self.get_queryset()
            serializer = CompanySerializer(qs, many=True)
            return GenericResponse(data=serializer.data ,approval=qs.info_company().values_list('approval', flat=True))


    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)
        return qs


