

from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import OrganizationInvite
from .serializers import OrganizationInviteSerializer, OrganizationInviteResponseSerializer

class OrganizationInviteListCreateView(generics.ListCreateAPIView):
    serializer_class = OrganizationInviteSerializer
    queryset = OrganizationInvite.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organization = request.user.get_organization()
        data = {
            "organization": organization,
            "sender": request.user,
            "message": request.data.get("message", ""),
        }
        serializer.create(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrganizationInviteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = OrganizationInviteResponseSerializer
    queryset = OrganizationInvite.objects.all()

    def get_object(self):
        try:
            obj = self.queryset.get(token=self.kwargs.get("token"))
            if obj.organization == self.request.user.get_organization() and obj.response == "PENDING":
                return obj
            raise NotFound("Invite not found or already responded")
        except OrganizationInvite.DoesNotExist:
            raise NotFound("Invite not found")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
