from rest_framework import serializers
from .models import Course
from user.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    Teacher = UserSerializer()

    class Meta:
        model = Course
        fields = '__all__'