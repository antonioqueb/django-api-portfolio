from rest_framework.serializers import ModelSerializer
from contact.models import ContactMe

class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactMe
        fields = '__all__'