# models
from apps.api.models import Entertainer, Venue, Event
# serializers
from apps.api.serializers.event import EventSerializer, EventSerializerV1
# rest framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.versioning import URLPathVersioning
from rest_framework.reverse import reverse
from django.http import JsonResponse

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			Event
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
    	versionControl = self.get_serializer_class()
    	queryset = self.get_queryset()
    	serializer = versionControl(queryset, many=True, context={'request': request})
    	return JsonResponse(serializer.data, safe=False)

    def get_queryset(self):
    	queryset = Event.objects.all()
    	id = self.request.query_params.get('id', None)
    	name = self.request.query_params.get('name', None)
    	entertainer = self.request.query_params.get('entertainer', None)
    	venue = self.request.query_params.get('venue', None)
    	date = self.request.query_params.get('date', None)
    	type = self.request.query_params.get('type', None)

    	queryset = queryset.filter(id=id) if id else queryset
    	queryset = queryset.filter(name__icontains=name) if name else queryset
    	queryset = queryset.filter(entertainer=entertainer) if entertainer else queryset
    	queryset = queryset.filter(venue=venue) if venue else queryset
    	queryset = queryset.filter(date__icontains=date) if date else queryset
    	queryset = queryset.filter(type__icontains=type) if type else queryset

    	return queryset

    def get_serializer_class(self):
    	if self.request.version == 'v1':
    		return EventSerializerV1
    	return EventSerializer

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.RetrieveAPIView):
	query_set = Event.objects.all()
	serializer_class = EventSerializer

	def get(self, request, id, format=None):
		versionControl = self.get_serializer_class()
		event = Event.objects.get(id=id)
		serializer = versionControl(event)
		return JsonResponse(serializer.data)

	def get_serializer_class(self):
		if self.request.version == 'v1':
			return EventSerializerV1
		return EventSerializer


class EventUpdate(GenericAPIView, UpdateModelMixin):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	lookup_field = 'id'

	def put(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

class EventDelete(GenericAPIView, DestroyModelMixin):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	lookup_field = 'id'

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
