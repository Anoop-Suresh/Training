from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=250,blank=True)
    email=models.EmailField(blank=True)
    phone = models.IntegerField(default=0,null=True)
    image = models.FileField(blank=True, upload_to='media/images/')
    friends = models.ManyToManyField("Profile", blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.name





#
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     likes = models.ManyToManyField(User, related_name='likes', blank=True)
#     # created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     # def publish(self):
#     #     self.published_date = timezone.now()
#     #     self.save()
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('list', args=[self.id])
#
#     def total_likes(self):
#         return self.likes.count()


class ImagePost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField()
    cover = models.FileField(blank=True, upload_to='media/images/')
    timestamp=models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def __str__(self):
        return self.title





class FriendRequest(models.Model):
    to_user=models.ForeignKey(User, related_name='to_user',on_delete=models.CASCADE)
    from_user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user',on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "From {}, to {}".format(self.from_user.username,self.to_user.username)

