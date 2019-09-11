from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('Resgister',views.Usercreate)#Register Url

router.register('Login', views.LoginViewSet, base_name='login')#Login URL

router.register('Addprofile',views.EditProfileView, base_name='Profile')

router.register('Newsfeed', views.FeedViewSet)

router.register("SendFriendRequest",views.FriendRequestViewSet,base_name='SendFriendRequest')

router.register('friendrequests',views.FriendshipRequestViewSet, base_name='friendrequests')


urlpatterns=[
    path('', include(router.urls)),]