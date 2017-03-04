from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_superuser(user):
    return user.is_superuser == True

def home(request):
    return render(request, 'home.html')

@user_passes_test(is_superuser)
def post(request):
    return render(request, 'post.html')
