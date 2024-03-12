from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.supabase import get_supabase_client
import json
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet

from project.serializers import ProjectTypeSerializer, ProjectTypeGetSerializer, ProjectSerializer, ProjectGetSerializer, ProjectGateSerializer


class ProjectGateView(ViewSet):
	
	@swagger_auto_schema( responses={200:ProjectGateSerializer(many=True)})
	def list(self,request):
		query = get_supabase_client("prj").table('gate_proyecto').select("*").order("id").eq("is_active",True).execute()
		return Response(query.data)

	@swagger_auto_schema( request_body=ProjectGateSerializer)
	def create(self,request):
		request_data = ProjectGateSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("gate_proyecto").insert(request_data.data).execute()
		return Response(query)
	
	@swagger_auto_schema(query_serializer=None, responses={204: None})
	def destroy(self, request, pk=None):
		query = get_supabase_client("prj").table("gate_proyecto").update({"is_active": False}).eq("id", pk).execute()
		return Response(query)
	
	@swagger_auto_schema(request_body=ProjectGateSerializer)
	def update(self,request,pk):
		request_data = ProjectGateSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("gate_proyecto").update(request_data.data).eq("id",pk).execute()
		return Response(query)


class ProjectTypeView(ViewSet):
	
	@swagger_auto_schema( responses={200:ProjectTypeGetSerializer(many=True)})
	def list(self,request):
		query = get_supabase_client("prj").table('proyecto_tipo').select("*").order("id").eq("is_active",True).execute()
		return Response(query.data)

	@swagger_auto_schema( request_body=ProjectTypeSerializer)
	def create(self,request):
		request_data = ProjectTypeSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("proyecto_tipo").insert(request_data.data).execute()
		return Response(query)
	
	@swagger_auto_schema(query_serializer=None, responses={204: None})
	def destroy(self, request, pk=None):
		query = get_supabase_client("prj").table("proyecto_tipo").update({"is_active": False}).eq("id", pk).execute()
		return Response(query)
	
	@swagger_auto_schema(request_body=ProjectTypeSerializer)
	def update(self,request,pk):
		request_data = ProjectTypeSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("proyecto_tipo").update(request_data.data).eq("id",pk).execute()
		return Response(query)
	

class ProjectView(ViewSet):
	
	@swagger_auto_schema( responses={200:ProjectGetSerializer(many=True)})
	def list(self,request):
		query = get_supabase_client("prj").table('proyectos_lista').select("*").order("id").eq("is_active",True).execute()
		return Response(query.data)
	
	@swagger_auto_schema( request_body=ProjectSerializer)
	def create(self,request):
		request_data = ProjectSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("proyectos").insert(request_data.data).execute()
		return Response(query)
	
	@swagger_auto_schema(query_serializer=None, responses={204: None})
	def destroy(self, request, pk=None):
		query = get_supabase_client("prj").table("proyectos").update({"is_active": False}).eq("id", pk).execute()
		return Response(query)
	
	@swagger_auto_schema(request_body=ProjectSerializer)
	def update(self,request,pk):
		request_data = ProjectSerializer(data=json.loads(request.body))
		validated_data = request_data.is_valid()
		query = get_supabase_client("prj").table("proyectos").update(request_data.data).eq("proyecto_id",pk).execute()
		return Response(query)
	


