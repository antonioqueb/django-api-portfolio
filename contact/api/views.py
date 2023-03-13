from rest_framework.viewsets import ModelViewSet
from contact.api.serializers import ContactSerializer
from contact.models import ContactMe

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication

class ContactViewSet(ModelViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactSerializer