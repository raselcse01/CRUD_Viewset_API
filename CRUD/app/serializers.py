from rest_framework import serializers
from app.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'gender', 'roll', 'email', 'waiver', 'date_of_birth', 'created_at']
        # fields = '__all__'