from rest_framework import serializers

# TIPO GATE
class GateTypeSerializer(serializers.Serializer):
	nombre = serializers.CharField()
	descripcion = serializers.CharField()	

class GateTypeGetSerializer(GateTypeSerializer):
	id = serializers.IntegerField()
