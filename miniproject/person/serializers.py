from csv import field_size_limit
from rest_framework import serializers
from .models import Deploy, Person

class Login_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['username','password']

class Signup_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','username','password']

class addRole_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['role']

class showRole_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
