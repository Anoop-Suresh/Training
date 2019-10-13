from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register', views.UserFormView.as_view(), name='register'),

    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('Profile/<int:pk>/', views.profile_detail, name='list'),
    path('edit',views.edit,name='edit'),
    path('newsfeed', views.newsfeed, name='newsfeed'),
    path('imagepost', views.ImagePostView.as_view(), name='imagepost'),
    path('friend-request/send/<int:pk>', views.send_friend_request,name='friendrequest'),
    path('friend-request/cancel/<int:pk>', views.cancel_friend_request,name='cancel'),
    path('friend-request/accept/<int:pk>', views.accept_friend_request,name='accept'),
    path('friend-request/delete/<int:pk>', views.delete_friend_request,name='delete'),

]

