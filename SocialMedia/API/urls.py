from django.urls import path,re_path
from . import views


urlpatterns=[
    #Profile
    path('profile', views.profileList.as_view(),name='proapi'),
    re_path(r'profile/(?P<pk>\d+)?$', views.profileapi.as_view(), name='proapi1'),

    #Image
    path('post', views.imageList.as_view(), name='imageapi'),

    #SearchAPI
    path('search',views.SearchList.as_view(),name='searchapi'),

    #FeiendRequest
    re_path(r'friendrequest/(?P<pk>\d+)?$', views.friendrequest.as_view(), name='friendrequest'),
    re_path(r'friendreceive/(?P<pk>\d+)?$', views.friendreceive.as_view(), name='friendreceive'),

    path('friends', views.FriendsList.as_view(), name='friends'),

    path('chat', views.ChatListView.as_view()),
    path('chat/create/', views.ChatCreateView.as_view()),
    path('chat/<pk>', views.ChatDetailView.as_view()),
    path('chat/<pk>/update/', views.ChatUpdateView.as_view()),
    path('chat/<pk>/delete/', views.ChatDeleteView.as_view())
]

