# models
from apps.api.models import Entertainer, Venue, Event
# serializer
from apps.api.serializers.venue import VenueSerializer, VenueSerializerV1
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
			VENUE
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    filter_fields = ('id', 'name', 'address', 'about')
    model = Venue

    def list(self, request):
    	versionControl = self.get_serializer_class()
    	queryset = self.get_queryset()
    	serializer = versionControl(queryset, many=True, context={'request': request})
    	return JsonResponse(serializer.data, safe=False)

    def get_queryset(self):
    	queryset = Venue.objects.all()
    	id = self.request.query_params.get('id', None)
    	name = self.request.query_params.get('name', None)
    	about = self.request.query_params.get('about', None)
    	address = self.request.query_params.get('address', None)

    	queryset = queryset.filter(id=id) if id else queryset
    	queryset = queryset.filter(name__icontains=name) if name else queryset
    	queryset = queryset.filter(about__icontains=about) if about else queryset
    	queryset = queryset.filter(address__icontains=address) if address else queryset

    	return queryset

    def get_serializer_class(self):
    	if self.request.version == 'v1':
    		return VenueSerializerV1
    	return VenueSerializer

    def post(self, request, format=None):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VenueDetail(generics.RetrieveAPIView):
	query_set = Venue.objects.all()
	serializer_class = VenueSerializer

	def get(self, request, id, format=None):
		versionControl = self.get_serializer_class()
		venue = Venue.objects.get(id=id)
		serializer = versionControl(venue)
		return JsonResponse(serializer.data)

	def get_serializer_class(self):
		if self.request.version == 'v1':
			return VenueSerializerV1
		return VenueSerializer

class VenueUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class VenueDelete(GenericAPIView, DestroyModelMixin):
	queryset = Venue.objects.all()
	serializer_class = VenueSerializer
	lookup_field = 'id'

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)