from rest_framework.views import APIView
from rest_framework.views import Response


class HelloAPIView (APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ Test get function """
        an_apiview = [
        'Uses HTTP Methods such as (get, post, put, patch, update, delete)',
        'Is Traditional to django view',
        'Gives most control over application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello !', 'an_apiview': an_apiview})

        
