from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from numba.cuda import match_any_sync
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class studentList(APIView):
    def get(self, request):
        student1 = Student.objects.all()
        serializer = StudentSerializer(student1, many=True)
        return Response(serializer.data)

    def post(self, request):
        data=JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def StudentListFinal(request,pk):
    try:
        stu=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='DELETE':
        stu.delete()
        return HttpResponse(status=204)
    if request.method=='GET':
        stu=StudentSerializer(stu)
        return JsonResponse(stu.data)
    if request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(stu,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    #
    #
    # def put(self,request):
    #     data = JSONParser().parse(request)
    #     serializer = StudentSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    # def delete(self,request,pk):
    #     stu=StudentSerializer.objects.get(pk=pk)
    #     stu.delete()
    #     return  HttpResponse(status=204)