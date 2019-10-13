from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Profile,ImagePost,FriendRequest
from chat.models import Chat

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields='__all__'

        def create(self, validated_data):
            return Profile.objects.create(**validated_data)


class imageSerializer(serializers.ModelSerializer):

    class Meta:
        model=ImagePost
        fields='__all__'


class friendrequestSerializer(serializers.ModelSerializer):

    class Meta:

        model = FriendRequest
        fields = '__all__'


class FriendsListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=[
            'id',
            'friends',
        ]




class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('__all__')

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('__all__')
