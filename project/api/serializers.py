from rest_framework.serializers import ModelSerializer
from project.models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'