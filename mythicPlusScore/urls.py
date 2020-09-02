from django.urls import path

from mythicPlusScore import views

urlpatterns = [
    path('', views.view_prior, name='past_list'),
    path('character/new/', views.search_new, name='search_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')


]
