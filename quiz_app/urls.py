from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover),
    path('addQuestion', views.addQuestion),
    path('register', views.register),
    path('kid_login', views.kid_login),
    path('adult_login', views.adult_login),
    path('quiz_lite', views.quiz_lite),
    # path('quiz_heavy', views.quiz_heavy),
    path('results', views.results),
    path('logout', views.logout)
]