from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """ Name Serializer """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """ creates and returns a new user """
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class profileFeedItemSerializer(serializers.ModelSerializer):
    """ Handles the Serializer of a Profile Feed """
    class Meta:
        model = models.UserProfileFeed
        fields = ('id', 'user_profile', 'status_field', 'created_on')
        extra_kwargs = {
        'user_profile':{
        'read_only':True
        }
        }
