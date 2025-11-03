from rest_framework import serializers
from restapi.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)


    def create(self , validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        print(instance)
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.age = validated_data.get('age',instance.age)
        instance.address = validated_data.get('address',instance.address)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.save()

        return instance


