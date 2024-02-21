from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.supabase import get_supabase_client

from supabase_auth.serializers import SignupSerializer

class SignupView(APIView):
	def post(self, request):
		serializer = SignupSerializer(data=request.data)
		if serializer.is_valid():
			email = serializer.validated_data['email']
			password = serializer.validated_data['password']

			user = get_supabase_client().auth.sign_up({"email":email, "password":password})
			# status = status.HTTP_200_OK

			return Response({"Message":user})

			# if error:
			#     return Response({"error": error.message}, status=status.HTTP_400_BAD_REQUEST)
			# else:
			#     return Response({"message": "Signup successful"}, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
	def post(self, request):
		serializer = SignupSerializer(data=request.data)
		if serializer.is_valid():
			email = serializer.validated_data['email']
			password = serializer.validated_data['password']

			user = get_supabase_client().auth.sign_in_with_password({"email":email, "password":password})
			# status = status.HTTP_200_OK

			return Response({"Message":user})

			# if error:
			#     return Response({"error": error.message}, status=status.HTTP_400_BAD_REQUEST)
			# else:
			#     return Response({"message": "Signup successful"}, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
