from django.shortcuts import render, get_object_or_404, redirect
from main.models import Blog
from .models import User

def mypage(request, id):
    user=get_object_or_404(User,id=id)
    context={
        'user':user,
        'blogs':Blog.objects.filter(writer=user),
        'followings':user.profile.followings.all(),
        'followers':user.profile.followers.all(),
    }
    return render(request,'users/mypage.html', context)

def follow(request,id):
    user=request.user
    followed_user=get_object_or_404(User,id=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
