from django.shortcuts import render, redirect, get_object_or_404
from .form import UserInputForm



# Create your views here.


def search_new(request):
    return render(request, 'MPS/home.html',)



#def default(request):
#   return render(request, 'post_detail.html',)
