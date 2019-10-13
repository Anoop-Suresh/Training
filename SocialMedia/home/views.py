from django.shortcuts import render,redirect
from.forms import UserForm,EditProfile,ImagePostForm
from django.views.generic import View,CreateView
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth,User
from .models import Profile,ImagePost,FriendRequest
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator



# Create your views here.


def home(request):

    return render(request,'login.html')


def profile(request):

    friends = request.user.profile.friends.all()
    sent_friend_requests = FriendRequest.objects.filter(from_user=request.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=request.user)

    context={'sent_friend_requests': sent_friend_requests,
             'rec_friend_requests': rec_friend_requests,
             'friends_list': friends,
            }
    return render(request,'profile.html',context)


class UserFormView(View):
    form_class = UserForm
    template_name= 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST , request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.image = form.cleaned_data.get('image')


            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form': form})





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            # messages.info(request, "Invalid USer")
            return redirect('register')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')



def search(request):
    if request.method == 'GET':
        word =  request.GET.get('search')
        try:
            status = Profile.objects.filter(name__icontains=word)
            #Add_prod class contains a column called 'bookname'
        except User.DoesNotExist:
            status = None
        return render(request,"profile.html",{"status":status})
    else:
        return render(request,"profile.html",{})

def profile_detail(request,pk):



    profile=User.objects.get(pk=pk)

    button_status = 'none'

    if profile not in request.user.profile.friends.all():
        button_status = 'not_friend'

        if len(FriendRequest.objects.filter(
                from_user=request.user).filter(to_user=profile)) == 1:
                button_status = 'friend_request_sent'

    context={'profile': profile,
             'button_status': button_status,
             }
    return render(request,"about.html",context)



def edit(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES , instance=request.user.profile)

        if form.is_valid():
            form.save()
            return render(request,'profile.html')

    else:
        form = EditProfile(instance=request.user.profile)
        args = {'form': form}
        return render(request, 'edit.html', args)




def newsfeed(request):
    image=ImagePost.objects.all().order_by('timestamp')
    paginator=Paginator(image,2)
    page=request.GET.get('page')
    image=paginator.get_page(page)
    context={'image':image}
    return render(request, 'Newsfeed.html', context)


class ImagePostView(CreateView): # new
    model = ImagePost
    form_class = ImagePostForm
    template_name = 'imagepost.html'
    success_url = reverse_lazy('newsfeed')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(ImagePostView,self).form_valid(form)




def send_friend_request(request,pk):
    # if request.user.is_authenticated():
        user=get_object_or_404(User,id=pk)
        frequest,created=FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user)
        return redirect('profile')

def cancel_friend_request(request,pk):
    # if request.user.is_authenticated():
        user=get_object_or_404(User,id=pk)
        frequest=FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user).first()
        frequest.delete()
        return redirect('profile')

def delete_friend_request(request,pk):
   from_user = get_object_or_404(User, id=pk)
   frequest = FriendRequest.objects.filter(
       from_user=from_user,
       to_user=request.user).first()
   frequest.delete()
   return redirect('profile')

def accept_friend_request(request,pk):
    from_user = get_object_or_404(User, id=pk)
    frequest = FriendRequest.objects.filter(
        from_user=from_user,
        to_user=request.user).first()
    user1=frequest.to_user
    user2=from_user
    user1.profile.friends.add(user2.profile)
    user2.profile.friends.add(user1.profile)
    frequest.delete()
    return redirect('profile')



def like_post(request):
    post=get_object_or_404(ImagePost, id=request.POST.get('post_id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True

    return HttpResponseRedirect(post.get_absolute_url())