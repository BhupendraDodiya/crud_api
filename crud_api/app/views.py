from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'DATA CREATED'}
            json_data = JSONRenderer().render(res)
            print(json_data)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
# Create your views here.
