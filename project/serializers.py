from rest_framework import serializers

# TIPOS DE PROYECTO
class ProjectTypeSerializer(serializers.Serializer):
	nombre = serializers.CharField()
	descripcion = serializers.CharField()
	num_stages = serializers.IntegerField()

class ProjectTypeDropdownSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	nombre = serializers.CharField()

class ProjectTypeGetSerializer(ProjectTypeSerializer):
	id = serializers.IntegerField()


# PROYECTOS
class ProjectSerializer(serializers.Serializer):
	nombre = serializers.CharField()
	fecha_fin_planeado = serializers.DateField()
	fecha_fin_estimado = serializers.DateField()
	proyecto_tipo_id = serializers.IntegerField()
	fase_gate_id = serializers.IntegerField()
	status = serializers.IntegerField()


class ProjectGetSerializer(ProjectSerializer):
	proyecto_id = serializers.IntegerField()