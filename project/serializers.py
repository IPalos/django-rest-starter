from rest_framework import serializers

class ProjectTypeSerializer(serializers.Serializer):
	nombre = serializers.CharField()
	descripcion = serializers.CharField()
	num_stages = serializers.IntegerField()

class ProjectTypeGetSerializer(ProjectTypeSerializer):
	id = serializers.IntegerField()


class ProjectSerializer(serializers.Serializer):
	nombre = serializers.CharField()
	tipo_proyecto_id = serializers.IntegerField()

class ProjectGetSerializer(ProjectSerializer):
	proyecto_id = serializers.IntegerField()