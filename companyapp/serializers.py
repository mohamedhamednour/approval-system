from rest_framework import serializers
from .models import Client , Company
from .conf import REQUIRED_FIELDS


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Client
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Company
        fields = '__all__'


    def validate(self, attrs):
        company_type = attrs.get("type", None)
        details = attrs.get("company_details", {})
        
        if company_type in REQUIRED_FIELDS:
            missing = [f for f in REQUIRED_FIELDS[company_type] if f not in details]
            if missing:
                raise serializers.ValidationError({
                    "company_details": f"Fields required for '{company_type}': {missing}"
                })
        return attrs


    

