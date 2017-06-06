from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Hello.models import Hello
from Hello.serializers import HelloSerializer

@csrf_exempt
#list all 
def Hello_list(request):
	if request.method == 'GET':
		Hellos=Hello.objects.all()
		serializer= HelloSerializer(Hellos,many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data= JSONParser().parse(request)
		serializer=HelloSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def Hello_detail(request,pk):
	#Retrieve, update or delete
	try:
		hello1= Hello.objects.get(pk=pk)
	except Hello.DoesNotExist:
		return HttpResponse(status=404)
	
	if request.method == 'GET':
		serializer = HelloSerializer(hello1)
		return JsonResponse(serializer.data)
        
	elif request.method:
		data =JSONParser().parse(request)
		serializer = HelloSerializer(hello1, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
                hello1.delete()
                return HttpResponse(status=204)
		
