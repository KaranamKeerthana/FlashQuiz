from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from testapp.models import Vocabulary,User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

# Create your views here.
@api_view(http_method_names=['GET'])
def display(req):
    data=list(Vocabulary.objects.values())
    return JsonResponse({'data':data})


@api_view(http_method_names=['POST'])
def register(req):
    data=req.body.decode("utf-8")
    print(data)
    data=json.loads(data)
    print(data)
    try:
        word=data['word']
        meaning=data['meaning']
        example=data['example']
        mnemonic=data['mnemonic']

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
    print(data)
    data=json.loads(data)
    print(data)
    
    try:
        username=data['username']
        print(username)
        password=data['password']
        print(password)

        data=User.objects.get(username=username)
        if(data.password==password):
            return HttpResponse("Logged in successfully")
        return HttpResponse("INVALID PASSWORD")
    except:
        return HttpResponse("USERNAME IS NOT FOUND")

# def logout(req):
#     logout(req)
#     return redirect('/')