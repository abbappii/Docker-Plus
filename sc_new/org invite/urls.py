from django.urls import path
from .views import OrganizationInviteListCreateView, OrganizationInviteRetrieveUpdateView

urlpatterns = [
    path("", OrganizationInviteListCreateView.as_view(), name="invite-list-create"),
    path("<str:token>/", OrganizationInviteRetrieveUpdateView.as_view(), name="invite-retrieve-update"),
]
