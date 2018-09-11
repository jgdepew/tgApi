# models
from apps.api.models import Entertainer
# serializers
from apps.api.serializers.entertainer import EntertainerSerializer, EntertainerSerializerV1
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
			ENTERTAINER
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
class EntertainerList(generics.ListAPIView):
    queryset = Entertainer.objects.all()
    serializer_class = EntertainerSerializer

    def list(self, request):
    	versionControl = self.get_serializer_class()
    	queryset = self.get_queryset()
    	serializer = versionControl(queryset, many=True, context={'request': request})
    	return JsonResponse(serializer.data, safe=False)

    def get_queryset(self):
    	id = self.request.query_params.get('id', None)
    	queryset = Entertainer.objects.all()
    	name = self.request.query_params.get('name', None)
    	about = self.request.query_params.get('about', None)
    	type = self.request.query_params.get('type', None)

    	queryset = queryset.filter(id=id) if id else queryset
    	queryset = queryset.filter(name__icontains=name) if name else queryset
    	queryset = queryset.filter(about__icontains=about) if about else queryset
    	queryset = queryset.filter(type__icontains=type) if type else queryset

    	return queryset

    def get_serializer_class(self):
    	if self.request.version == 'v1':
    		return EntertainerSerializerV1
    	return EntertainerSerializer

    def post(self, request, format=None):
        serializer = EntertainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntertainerDetail(generics.RetrieveAPIView):
	query_set = Entertainer.objects.all()
	serializer_class = EntertainerSerializer

	def get(self, request, id, format=None):
		versionControl = self.get_serializer_class()
		entertainer = Entertainer.objects.get(id=id)
		serializer = versionControl(entertainer)
		return JsonResponse(serializer.data)

	def get_serializer_class(self):
		if self.request.version == 'v1':
			return EntertainerSerializerV1
		return EntertainerSerializer


class EntertainerUpdate(GenericAPIView, UpdateModelMixin):
	queryset = Entertainer.objects.all()
	serializer_class = EntertainerSerializer
	lookup_field = 'id'

	def put(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

class EntertainerDelete(GenericAPIView, DestroyModelMixin):
	queryset = Entertainer.objects.all()
	serializer_class = EntertainerSerializer
	lookup_field = 'id'

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)