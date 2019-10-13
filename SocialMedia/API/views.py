from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import profileSerializer,imageSerializer,friendrequestSerializer,FriendsListSerializer,ChatSerializer
from home.models import Profile,ImagePost,FriendRequest
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .pagination import PostPageNumberPagination
from rest_framework import generics
from chat.models import Chat,Contact
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()
# Create your views here.
class profileList(APIView):


    def get(self,request):
        profile=Profile.objects.all()
        serializer=profileSerializer(profile,many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class profileapi(APIView):
    def get(self,request,pk):
        proj=Profile.objects.filter(id=pk)
        serializer=profileSerializer(proj,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class searchapi(APIView):

    def get_queryset(self):
        qs = Profile.objects.all()



class imageList(ListAPIView):

    queryset=ImagePost.objects.all()
    serializer_class= imageSerializer
    pagination_class = PostPageNumberPagination



class SearchList(generics.ListAPIView):
    serializer_class = profileSerializer

    def get_queryset(self):
        qs=Profile.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(name__icontains=query).distinct()
        return qs



# class friendrequest(APIView):
#
#
#     def get(self,request):
#         profile=FriendRequest.objects.all()
#         serializer=friendrequestSerializer(profile,many=True)
#         return Response(serializer.data)
#
#
#     def post(self):
#         pass


class friendrequest(APIView):
    def get(self,request,pk):
        frie=FriendRequest.objects.filter(from_user=pk)
        serializer=friendrequestSerializer(frie,many=True)
        return Response(serializer.data)
    def post(self):
        pass


class friendreceive(APIView):
    def get(self,request,pk):
        frie=FriendRequest.objects.filter(to_user=pk)
        serializer=friendrequestSerializer(frie,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class FriendsList(ListAPIView):
    queryset=Profile.objects.filter()
    serializer_class = FriendsListSerializer



def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact, user=user)
    return contact




class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )