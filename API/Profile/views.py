from django.shortcuts import render
from django.shortcuts import render
import git
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from Profile.models import ProfileDB
from Profile.serializers import ProfileSerializer
from rest_framework.decorators import api_view
from bson import ObjectId

from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def profileApi(request):
    if request.method == 'POST':
        profile_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse(profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        profile_data = ProfileDB.objects.all()
        profile_serializer = ProfileSerializer(profile_data, many=True)
        return JsonResponse(profile_serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def profileDetails(request, id):
    try:
        if request.method == 'GET':

            profile_data = ProfileDB.objects.get(_id=ObjectId(id))
            profile_serializer = ProfileSerializer(profile_data)
            if profile_serializer:
                return JsonResponse(profile_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            profile_data = JSONParser().parse(request)
            profile = ProfileDB.objects.get(_id=ObjectId(id))
            profile_serializer = ProfileSerializer(profile, data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return JsonResponse(profile_serializer.data)

        elif request.method == 'DELETE':
            profile_data = ProfileDB.objects.get(_id=ObjectId(id))
            profile_data.delete()
            return JsonResponse({'message': 'Profile were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except ProfileDB.DoesNotExist:
        return JsonResponse({"status": 404, "success": False, 'message': 'Data Not Found!'}, status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':

    #     profile_data =ProfileDB.objects.get(_id=ObjectId(id))
    #     profile_serializer = ProfileSerializer(profile_data)
    #     if profile_serializer :
    #         return JsonResponse(profile_serializer.data,status=status.HTTP_200_OK)
    #     return JsonResponse({profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'PUT':
    #     profile_data = JSONParser().parse(request)
    #     profile=ProfileDB.objects.get(_id=ObjectId(id))
    #     profile_serializer = ProfileSerializer(profile, data=profile_data)
    #     if profile_serializer.is_valid():
    #         profile_serializer.save()
    #         return JsonResponse(profile_serializer.data)
    #     return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     profile_data = ProfileDB.objects.get(_id=ObjectId(id))
    #     profile_data.delete()
    #     return JsonResponse({'message': 'Profile were deleted successfully!'},status=status.HTTP_204_NO_CONTENT)


# SHA256:k4roWrGbSIVRx9Q+IoZu6B+KO1F8mTa32dgc5qxmCyU


@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("sangeetapaswan.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere!...")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere.")






