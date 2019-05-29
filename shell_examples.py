from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status


#serialize a single object
obj=Status.object.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)
stream=BytesIO(json_data)
data=JSONParser().parse(stream)
print(data)


#serialize a queryset
qs=Status.object.all()
serializer2=StatusSerializer(qs, many=True)
serializer2.data
json_data2=JSONRenderer().render(serializer2.data)
print(json_data2)

stream2=BytesIO(json_data2)
data2=JSONParser().parse(stream2)
print(data2)


#create object
data = {'user':1}
create_serializer = StatusSerializer(data=data)
create_serializer.is_valid()
create_serializer.save()


#update object
obj=Status.object.first()
data={'user':1, 'content':'Some updated content'}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()



#delete object
data = {'user':1, 'content':'please delete me'}
create_serializer = StatusSerializer(data=data)
create_serializer.is_valid()
created_obj = create_serializer.save()
print(created_obj)

obj = status.objects.last()
get_data_serializer = StatusSerializer(obj)
print(obj.delete())
