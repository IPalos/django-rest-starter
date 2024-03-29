from django.urls import include, path, re_path

from project.views import ProjectTypeView, ProjectView, ProjectGateView

urlpatterns = [
	path("project_types/", ProjectTypeView.as_view({
		"get":"list",
		"post":"create"
		})),
	path("project_types/<int:pk>",ProjectTypeView.as_view({
		"patch":"update",
		"delete":"destroy"
		})),
	path("projects/", ProjectView.as_view({
		"get":"list",
		"post":"create"
		})),
	path("projects/<int:pk>",ProjectView.as_view({
		"patch":"update",
		"delete":"destroy"
		})),

	path("gate-proyecto/", ProjectGateView.as_view({
		"get":"list",
		"post":"create"
		})),
	path("gate-proyecto/<int:pk>",ProjectGateView.as_view({
		"patch":"update",
		"delete":"destroy"
		})),
]