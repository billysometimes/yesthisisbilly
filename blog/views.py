from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Post, Tag
from .forms import PostForm
def is_superuser(user):
    return user.is_superuser == True

def home(request):
    return render(request, 'home.html')

def blog(request):
    post_list = Post.objects.order_by('-publish_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog.html', context)

@user_passes_test(is_superuser)
def submit(request):
    form = PostForm(request.POST)
    post = form.save(commit=False)
    post.author = request.user
    post.save()

    for tag in form.cleaned_data.get('tags'):
        post.tags.add(tag)
    post.save()
    return redirect('/blog/')

@user_passes_test(is_superuser)
def post(request):
    return render(request, 'post.html', {'post': PostForm()})
