from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from testing_api.serializers import UserSerializer, SnippetSerializer
from testing_api.models import User, Snippet
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET', 'POST'])
def users_list(request):

    if request.method == "GET":
        users = User.objects.all()

        users = UserSerializer(users, many=True)
        return JsonResponse(users.data, safe=False)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def snippet_list(request):

    if request.method == 'GET':

        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':

        print(request.POST)

        data = JSONParser().parse(request)

        print(data)

        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    


@csrf_exempt
def snippets_detail(request, pk):

    try:
        snippet = Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)

        return Response(serializer.data, safe=False)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = SnippetSerializer(snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=False)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':

        data = JSONParser().parse(request)

        serializer = SnippetSerializer(snippet, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, safe=False)

        return Response(serializer.errors, status=400)


    

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)