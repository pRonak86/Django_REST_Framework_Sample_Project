from rest_framework import  serializers
from myApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields='__all__'
        fields=['id','StudentName','StudentLastName','StudentContact']

