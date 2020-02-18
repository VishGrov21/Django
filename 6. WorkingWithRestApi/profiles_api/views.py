from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication


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

        return Response({'message': 'Hello !', 'an_apiview': an_apiview})

    def post(self, request):
        """ Hello Message with Name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating of an object """
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """ Handles patching of an object """
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """ Handles deleting of an object """
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test APIViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Returns a Hello Message """
        a_viewset = [
            'Uses actions such as (list, create, retrieve, update, partial_update, delete)',
            'Automaticaaly maps to URLs using Routers',
            'Provides more functionality with lesser code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def retrieve(self, request, pk=None):
        """ Handles getting an object by its ID """
        return Response({'HTTP_METHOD': 'GET'})

    def create(self, request):
        """ Create a new Hello Message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """ Handles getting an object by its ID """
        return Response({'HTTP_METHOD': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles getting an object by its ID """
        return Response({'HTTP_METHOD': 'patch'})

    def destroy(self, request, pk=None):
        """ Handles getting an object by its ID """
        return Response({'HTTP_METHOD': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    # django rest framework is aware of the standard functions that developer would like to
    # perform on a model viewset, like Create, list, update, partial update
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchField,)
    search_fiels = ('name', 'email',)
