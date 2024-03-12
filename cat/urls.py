from django.urls import include, path, re_path

from project.views import ProjectTypeView, ProjectView
from cat.views import StatusView

urlpatterns = [
	path("status/", StatusView.as_view({
		"get":"list"
	}))
	# path("project_types/", ProjectTypeView.as_view({
	# 	"get":"list",
	# 	"post":"create"
	# 	})),
	# path("project_types/<int:pk>",ProjectTypeView.as_view({
	# 	"patch":"update",
	# 	"delete":"destroy"
	# 	})),
	# path("projects/", ProjectView.as_view({
	# 	"get":"list",
	# 	"post":"create"
	# 	})),
	# path("projects/<int:pk>",ProjectView.as_view({
	# 	"patch":"update",
	# 	"delete":"destroy"
	# 	}))
]