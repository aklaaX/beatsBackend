from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.response import Response
from rest_framework import status

from Beats.models import Beat
from Beats.serializer import BeatSerializer

class BeatViewSet(ModelViewSet):
    serializer_class = BeatSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)

        # Parser manuellement le JWT sans vérification
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        try:
            backend = TokenBackend(algorithm="HS256", signing_key=None)
            payload = backend.decode(token, verify=False)
            request.jwt_payload = payload
        except Exception:
            request.jwt_payload = {}
        return request

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        if not hasattr(request, "jwt_payload") or "user_id" not in request.jwt_payload:
            raise NotAuthenticated("Authentication required.")

    def get_queryset(self):
        role = self.request.jwt_payload.get("role", "User")
        return Beat.objects.all() if role == "Admin" else Beat.objects.filter(isPublished=True)

    def perform_create(self, serializer):
        role = self.request.jwt_payload.get("role", "User")
        if role == "Admin":
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to create this beat.")

    def perform_update(self, serializer):
        role = self.request.jwt_payload.get("role", "User")
        if role == "Admin":
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to update this beat.")

    def perform_destroy(self, instance):
        role = self.request.jwt_payload.get("role", "User")
        if role == "Admin":
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this beat.")