from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView (APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Test get function """
        an_apiview = [
        'Uses HTTP Methods such as (get, post, put, patch, update, delete)',
        'Is Traditional to django view',
        'Gives most control over application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello !', 'an_apiview': an_apiview})

    def post(self,request):
        """ Hello Message with Name """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handles updating of an object """
        return Response({'message':'PUT'})


    def patch(self, request, pk=None):
        """ Handles patching of an object """
        return Response({'message':'PATCH'})


    def delete(self, request, pk=None):
        """ Handles deleting of an object """
        return Response({'message':'DELETE'})
