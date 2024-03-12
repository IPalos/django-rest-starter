from rest_framework import serializers

class StatusSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	nombre = serializers.CharField()
	tipo = serializers.CharField()
