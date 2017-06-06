from rest_framework import serializers
from Hello.models import Hello
	
class HelloSerializer(serializers.Serializer):
	id=serializers.IntegerField(read_only=True)
	name= serializers.CharField(required=False, allow_blank=True, max_length=100)
	title=serializers.CharField(required=False, allow_blank=True, max_length=100)
	event=serializers.CharField(style={'base_template': 'textarea.html'})
	start_time=serializers.DateTimeField(allow_null=True)#,allow_blank=False)
	end_time=serializers.DateTimeField(allow_null=True)#,allow_blank=False)
	created=serializers.DateTimeField(read_only=True)
	
	def create(self, vailidated_data):
		#when create a new event, give the vailidated_data
		return Hello.objects.create(**vailidated_data)
	def update(self,vailidated_data, instance):
		# update, return an existing 'Hello', give validated data
		instance.name=vailidated_data.get('name',instance.name)
		instance.title=vailidated_data.get('title',instance.title)
		instance.event=vailidated_data.get('event',instance.event)
		instance.start_time=vailidated_data.get('start_time',instand.start_time)
		instance.end_time=vailidated_data.get('end_time',instance.end_time)
		instance.created=vailidated_data.get('created',instance.created)
		instance.save()
		return instance