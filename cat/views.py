from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from main.supabase import get_supabase_client
from rest_framework.response import Response
import json
from rest_framework.viewsets import ViewSet

from cat.serializers import StatusSerializer

# Create your views here.
class StatusView(ViewSet):
	
	@swagger_auto_schema( responses={200:StatusSerializer(many=True)})
	def list(self,request):
		query = get_supabase_client("cat").table('status').select("*").order("id").execute()
		return Response(query.data)

	# @swagger_auto_schema( request_body=ProjectTypeSerializer)
	# def create(self,request):
	# 	request_data = ProjectTypeSerializer(data=json.loads(request.body))
	# 	validated_data = request_data.is_valid()
	# 	query = get_supabase_client("prj").table("proyecto_tipo").insert(request_data.data).execute()
	# 	return Response(query)
	
	# @swagger_auto_schema(query_serializer=None, responses={204: None})
	# def destroy(self, request, pk=None):
	# 	query = get_supabase_client("prj").table("proyecto_tipo").update({"is_active": False}).eq("id", pk).execute()
	# 	return Response(query)
	
	# @swagger_auto_schema(request_body=ProjectTypeSerializer)
	# def update(self,request,pk):
	# 	request_data = ProjectTypeSerializer(data=json.loads(request.body))
	# 	validated_data = request_data.is_valid()
	# 	query = get_supabase_client("prj").table("proyecto_tipo").update(request_data.data).eq("id",pk).execute()
	# 	return Response(query)
	