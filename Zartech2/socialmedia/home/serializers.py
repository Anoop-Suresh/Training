from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,NewsFeedItem
from . import services as likes_services
from friendship.models import FriendshipRequest,Friend



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id','username','email','password')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user






class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model= Profile
        fields='__all__'
        extra_kwargs = {'user': {'read_only': True}}



class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()





class FeedSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = NewsFeedItem
        fields = (
            'id',
            'user_profile', 'cover','status_text', 'created_on',
            'is_fan',
            'total_likes',
        )
        extra_kwargs = {'user_profile': {'read_only': True}}

    def get_is_fan(self, obj) -> bool:
        """Check if a `request.user` has liked this tweet (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)



class FriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendshipRequest
        fields = ('id', 'from_user', 'to_user')
        extra_kwargs = {'from_user': {'read_only': True}}




class FriendshipRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendshipRequest
        fields = ('id', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')





