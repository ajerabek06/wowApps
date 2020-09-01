from django.urls import path

from mythicPlusScore import views

urlpatterns = [
    path('', views.search_new, name="MythicPlusScores"),


]
