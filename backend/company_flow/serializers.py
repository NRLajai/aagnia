from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id", "name", "company_details", "tag", "status", "follow_up_date", "phone_number", "image"]

