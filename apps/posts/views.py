from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.posts.forms import PostForm
from apps.posts.models import Post


def index(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'home.html', context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = PostForm()
