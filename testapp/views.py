from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from testapp.models import Vocabulary,User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json,random

# Create your views here.
@api_view(http_method_names=['GET'])
def display(req):

    data=list(Vocabulary.objects.values())
    data = random.shuffle(data)
    if len(data) >= 10:
        data = data[:10]
    return JsonResponse({'data':data})


@api_view(http_method_names=['GET'])
def getData(req):
    data=list(Vocabulary.objects.values())
    return Response({'data':data}, status=HTTP_200_OK)



@api_view(http_method_names=['POST'])
def register(req):
    data=req.body.decode("utf-8")
    data=json.loads(data)
    try:
        word=data['word'].capitalize()
        meaning=data['meaning'].capitalize()
        example=data['example'].capitalize()
        mnemonic=data['mnemonic'].capitalize()

        data=Vocabulary(word=word,meaning=meaning,example=example,mnemonic=mnemonic)
        data.save()
        return HttpResponse("Data registered successfully")
    except Exception as error:
        return Response({"error":error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



@api_view(http_method_names=['POST'])
def signup(req):
    data=req.body.decode("utf-8")
    data=json.loads(data)
    try:
        username=data['username']
        password=data['password']
        data=User(username=username,password=password)
        data.save()
        
        return HttpResponse("Data registered successfully")
    except Exception as error:
        return Response({"error":error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(http_method_names=['POST'])
def signin(req):
    data=req.body.decode("utf-8")
    data=json.loads(data)
    
    try:
        username=data['username']
        password=data['password']

        data=User.objects.get(username=username)
        if(data.password==password):
            return HttpResponse("Logged in successfully")
        return HttpResponse("INVALID PASSWORD")
    except:
        return Response({"error":"USERNAME IS NOT FOUND"}, status=status.HTTP_403_FORBIDDEN)
