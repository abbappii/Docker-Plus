from rest_framework import serializers

from .models import OrganizationInvite
from .choices import OrganizationInviteResponse


class OrganizationInviteSerializer(serializers.ModelSerializer):
    target = serializers.StringRelatedField()
    sender = serializers.StringRelatedField()
    organization = serializers.StringRelatedField()

    class Meta:
        model = OrganizationInvite
        fields = [
            "id",
            "target",
            "message",
            "response",
            "token",
            "sender",
            "organization",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["token", "created_at", "updated_at"]


class OrganizationInviteResponseSerializer(serializers.Serializer):
    response = serializers.ChoiceField(choices=OrganizationInviteResponse.choices)


