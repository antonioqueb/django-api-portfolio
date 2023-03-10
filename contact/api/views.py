from rest_framework.viewsets import ModelViewSet
from contact.api.serializers import ContactSerializer
from contact.models import ContactMe


class ContactViewSet(ModelViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactSerializer