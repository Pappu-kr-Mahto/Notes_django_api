from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
    
    def validate(self, data):
        if User.objects.filter(email=data['email']).exists() or User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"error":'User already Exists with this Username/Email'})
        return data
    
    def create(self,data):
        user=User.objects.create_user(username=data['username'] , email=data['email'],password=data['password'])
        print("created successfully")
        return data

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesTable
        fields = '__all__'

class IdSerializer(serializers.Serializer):
    id=serializers.IntegerField()

    def validate_id(self , value):
        if not isinstance(value,int):
            raise serializers.ValidationError({"error":"Note id must be an Integer"})
        else:
            if NotesTable.objects.filter(id =value).exists():
                return value
            else:
                raise serializers.ValidationError({"error":"Notes for the corresponding id is not available"})