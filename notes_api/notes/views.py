from django.shortcuts import HttpResponse
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response
from rest_framework import status

import datetime
# Create your views here.

def home(request):
    return HttpResponse("Welcome home")


@api_view(['POST'])
def signup(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    print(request.data)
    try:
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        
        if username_or_email is None or password is None:
            return Response({'message': 'Please provide both username/email and password'}, status=status.HTTP_400_BAD_REQUEST)

        if '@' in username_or_email:
            print("email")
            temp = User.objects.filter(email=request.data.get("username_or_email")).exists()

            if(temp):
                user = authenticate( email=username_or_email, 
                password=password)
            else:
                return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)

        else:
            print("username")
            temp = User.objects.filter(username=request.data.get("username_or_email")).exists()
            if(temp):
                user = authenticate( username=username_or_email, password=password)
            else:
                return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
            
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                    'user':request.data['username_or_email'],
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })
    except Exception as e:
        return Response(e,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crateNote(request):
    try:
        user=User.objects.get(username=request.user)
        print(user)
        version=[{"note":request.data['note'],"updated_at":datetime.datetime.now()}]
        data = NotesTable.objects.create(userId=user,note=request.data['note'],versions=version)
        return Response({"success":"notes created successfully"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allNotes(request):
    try:
        notes=NotesTable.objects.all().values()
        # print(notes)
        # serializer = NotesSerializer(data=notes,partial=True)

        # if serializer.is_valid():
        #     print(serializer.data)
        # else:
        #     print(serializer.errors)
            
        # print(serializer.data)
        return Response(notes)
    except Exception as e:
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def notesById(request,id):

    if request.method == "GET":
        try:
            data = NotesTable.objects.filter(id=id).values()
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == "POST":
        try:
            obj=NotesTable.objects.get(id=id)
            obj.note=request.data['note']
            versions=eval(obj.versions)
            versions.insert(0,{"note":request.data['note'],"updated_at":datetime.datetime.now()})
            obj.versions=versions
            obj.save()
            return Response({"success":"updated successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shareNotes(request):
    try:
        # print(request.data)
        note=NotesTable.objects.filter(id=request.data['noteId']).first()
        users=eval(request.data['usernames'])
        for usr in users:
            user=User.objects.get(username=usr)
            version=[{"note":note.note,"updated_at":datetime.datetime.now()}]
            print(version)
            data = NotesTable.objects.create(userId=user,note=note.note,versions=version)
        return Response(request.data)
    except Exception as e:
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notesVersion(request,id):
    try:
        note=NotesTable.objects.filter(id=id).values("versions")
        return Response(note)
    except Exception as e:
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)