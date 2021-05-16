from django.shortcuts import render
# jsonResponse will return in Json format below
from django.http import request, JsonResponse
from .models import Employee
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# here below is functionn based view

@csrf_exempt
def EmployeeDetails(request):
    if request.method == "GET":
        obj = Employee.objects.all()  # Query to get the values
        # getting the values in dictionary format below
        data = {"responseValue": list(obj.values("id", "name"))}
        return JsonResponse(data)

    elif request.method == "POST":
        # # assaign the value to a variable called name1
        # name = request.POST["name"]
        # # Passthing this variable to Employee models name column
        # obj = Employee(name=name)
        # obj.Save()  # Executing the obj
        # # serialzing the data
        # data = {"response": {"id": obj.id, "name": obj.name}}
        # return JsonResponse(data)
        name1 = request.POST["name"]
        obj = Employee(name=name1)
        obj.save()
        data = {"response":{"id":obj.id, "name":obj.name}}
        return JsonResponse(data)
# here below is class based view


class ListEmployee(View):  # same as before but this time its classed based
    def get(self, request):
        obj = Employee.objects.all()
        data = {"response": list(obj.values("id", "name"))}
        return JsonResponse(data)

    def post(self, request):
        name1 = request.POST("name")
        obj = Employee(name=name1)
        obj.save()
        data = {"response": {"id": obj.id, "name": obj.name}}
        return JsonRequest(data)
