from django.urls import include, path, re_path

from gate.views import GateTypeView

urlpatterns = [
	path("gate_types/", GateTypeView.as_view({
		"get":"list",
		"post":"create"
		})),
	path("gate_types/<int:pk>",GateTypeView.as_view({
		"patch":"update",
		"delete":"destroy"
		})),
]