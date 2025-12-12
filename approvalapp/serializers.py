from .models import Approval
from rest_framework import serializers
from rest_framework.response import Response



class ApprovalSerializer(serializers.ModelSerializer):
    approved_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Approval
        fields = '__all__'


