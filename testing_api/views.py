from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from testing_api.serializers import UserSerializer
from testing_api.models import User, Snippet
# Create your views here.

@csrf_exempt
def users_list(request):

    if request.method == "GET":
        users = User.objects.all()

        users = UserSerializer(users, many=True)
        return JsonResponse(users.data, safe=False)

@csrf_exempt
def snippet_list(request):

    if request.method == 'GET':

        snippets = Snippet.objects.all()
    