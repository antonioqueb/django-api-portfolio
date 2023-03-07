from rest_framework.serializers import ModelSerializer
from me.models import Me

class MeSerializer(ModelSerializer):
    class Meta:
        model = Me
        fields = '__all__'
