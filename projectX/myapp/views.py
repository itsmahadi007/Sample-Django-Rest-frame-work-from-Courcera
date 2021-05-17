from django.shortcuts import render
# jsonResponse will return in Json format below
from django.http import request, JsonResponse
from .models import Employee
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# here below is functionn based view


@csrf_exempt
@api_view(['POST'])
def EmployeeDetails(request):
    if request.method == "GET":
        obj = Employee.objects.all()  # Query to get the values
        # getting the values in dictionary format below
        data = {"responseValue": list(obj.values("id", "name"))}
        return Response(data)

    elif request.method == "POST":
        # # assaign the value to a variable called name1
        # # Passthing this variable to Employee models name column
        # # serialzing the data

        name1 = request.data["name"]
        obj = Employee(name=name1)
        obj.save()
        data = {"response": {"id": obj.id, "name": obj.name}}
        return Response(data)
# here below is class based view


class ListEmployee(APIView):

    def get(self, request):
        obj = Employee.objects.all()  # Query to get the values
        # getting the values in dictionary format below
        data = {"responseValue": list(obj.values("id", "name"))}
        return Response(data)
        #return Response(data, status="", headers="", template_name="", content_type="")

    def post(self, request):
        name1 = request.data["name"]
        obj = Employee(name=name1)
        obj.save()
        data = {"response": {"id": obj.id, "name": obj.name}}
        return Response(data)
