from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Game as gameModel
from api.models import actualGame

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List': '/task-list/',
		'Detail View': '/task-detail/<str:pk>/',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>/',
		'Delete': '/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def addName(request):

    return JsonResponse({'data': list(gameModel.objects.values())})


@api_view(['GET'])
def set_name(request, pk):
	new = gameModel.objects.get(id=1)
	new.player_name = pk
	new.save()
	return JsonResponse({'data': list(gameModel.objects.values())})
	
@api_view(['GET'])
def returnData(request):
    return JsonResponse({'data': list(gameModel.objects.values())})
    

@api_view(['GET'])
def getname(request):
	gg = gameModel.objects.get(id=1)
	return Response(gg.player_name)

@api_view(['GET'])
def reset_settings(request):
	gameData = actualGame.objects.get(id=1)
	gameData.attempts_left = 7
	gameData.word_length = 0
	gameData.attemptDone = False
	gameData.save()
	return Response(Response.status_code)


	
@api_view(['GET'])
def showDaddy(request):
	gameData = actualGame.objects.get(id=1)
	print(gameData)
	return Response(Response.status_code)





