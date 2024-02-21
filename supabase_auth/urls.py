from django.urls import include, path, re_path

from supabase_auth.views import SignupView, SignInView


urlpatterns = [
	path("register/", SignupView.as_view()),
	path("login/", SignInView.as_view())

]