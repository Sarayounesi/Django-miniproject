from pstats import Stats
from urllib import response
from myapp.models import Deploy, Person
from .serializers import Login_serializer, Signup_serializer, addLog_serializer, showLog_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
import jwt
from Tools.auth import *
from person import serializers

@api_view(['POST'])
def sign_up(request):
    serializer = Signup_serializer(data = request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        person = Person.objects.filter(username = username).first()
        if not person:
            serializer.save(password = make_password(password))
            return Response('OK', status = 200)
        else:
            return Response('NOT OK', status = 401)
    else:
        return Response('bad request',status=400)


@api_view(['POST'])
def log_in(request):
    serializer = Login_serializer(data = request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        person = Person.objects.filter(username = username).first()
        if person and check_password(password, person.password):
            encoded_jwt = jwt.encode({'username': person.username},"fcgvjbhknkcgvhjbkcvhbjnui465hvgcfd",algorithm="HS256")
            response = Response('OK', status=200)
            response.set_cookie('Token', encoded_jwt)
            return response
        else:
            return Response('NOT OK', status = 401)
    else:
        return Response('',status=400)


@api_view(['POST'])
@role_req("user")
def add_person_object(request,person):
    serializer = addRole_serializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save(person_name = person.name)
        return Response('OK', status = 200)
    else:
        return Response('NOT OK', status = 401)


@api_view(['GET'])
@role_req("user")
def get_person_objects(request):
    persons = Person.objects.all()
    serialize = showRole_serializer(persons, many=True)
    return Response(serialize.data, status=200)
