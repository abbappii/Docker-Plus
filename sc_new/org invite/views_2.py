from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrganizationInviteSerializer
from .models import OrganizationInvite

class OrganizationInviteCreateView(generics.CreateAPIView):
    queryset = OrganizationInvite.objects.all()
    serializer_class = OrganizationInviteSerializer

    def post(self, request, *args, **kwargs):
        organization = request.user.get_organization()
        serializer = self.get_serializer(data={
            "organization": organization,
            "sender": request.user,
            "message": request.data.get("message", ""),
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrganizationInviteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = OrganizationInvite.objects.all()
    serializer_class = OrganizationInviteSerializer

    def get_queryset(self):
        return self.queryset.filter(
            organization=self.request.user.get_organization(),
            status="PENDING"
        )

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    