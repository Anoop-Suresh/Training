from django.shortcuts import render
from .serializers import UserSerializer,ProfileSerializer,FeedSerializer,FriendRequestSerializer,FriendshipRequestSerializer
from rest_framework import viewsets,status
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Profile,NewsFeedItem
from rest_framework.authentication import TokenAuthentication
from . import permissions
from .mixins import LikedMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .pagination import PostPageNumberPagination
from friendship.models import Friend,FriendshipRequest
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action





# Create your views here.
#Register API view
class Usercreate(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    # For Search Option
    filter_backends = (filters.SearchFilter,)
    search_fields=('username',)



#Login API
class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)






# Edit Profile API

class EditProfileView(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    # queryset = Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    def get_queryset(self):
        user=self.request.user
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user=self.request.user)






class FeedViewSet(LikedMixin,
                   viewsets.ModelViewSet):

        queryset = NewsFeedItem.objects.all().order_by('-created_on')
        serializer_class = FeedSerializer
        permission_classes = (permissions.PostOwnStatus,IsAuthenticated )
        pagination_class = PostPageNumberPagination

        def perform_create(self, serializer):
            """Sets the user profile to the logged in user."""

            serializer.save(user_profile=self.request.user)




class FriendRequestViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = FriendRequestSerializer
    # queryset = FriendshipRequest.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user=self.request.user
        return FriendshipRequest.objects.filter(from_user=user)




    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(from_user=self.request.user)

    @action(methods=['get'],detail=True)

    def cancel(self, request, pk=None):
         friendship_request = get_object_or_404(FriendshipRequest, pk=pk, from_user=request.user)
         friendship_request.cancel()
         return Response(
             FriendshipRequestSerializer(friendship_request).data,
             status.HTTP_201_CREATED
         )




class FriendshipRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for FriendshipRequest model
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = FriendshipRequestSerializer

    def get_queryset(self):
        user=self.request.user
        return FriendshipRequest.objects.filter(to_user=user)


    @action(methods=['get'],detail=True)
    def accept(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.accept()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )

    @action(methods=['get'],detail=True)
    def reject(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.reject()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )
