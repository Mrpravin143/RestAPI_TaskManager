from rest_framework import serializers
from restapi.models import Student

class StudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Student

        fields = "__all__"