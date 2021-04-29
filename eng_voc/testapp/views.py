from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from testapp.models import Vocabulary
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
    data=json.loads(data)
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
    
   

