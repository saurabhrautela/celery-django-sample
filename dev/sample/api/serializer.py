from rest_framework import serializers


class MathOperationSerializer(serializers.Serializer):
    operation = serializers.CharField(required=True, max_length=25)
    data = serializers.JSONField()

