from django.contrib import admin
from .models import Profile,ImagePost,FriendRequest

# Register your models here.

admin.site.register(Profile)
# admin.site.register(Post)
admin.site.register(ImagePost)
admin.site.register(FriendRequest)

