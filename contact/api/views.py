from rest_framework.viewsets import ModelViewSet
from contact.api.serializers import ContactSerializer
from contact.models import Contact


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer