from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover),
    path('addQuestion', views.addQuestion),
    path('logreg', views.logreg),
    path('register', views.register),
    path('kid_login', views.kid_login),
    path('adult_login', views.adult_login),
    path('start_lite/<int:user_id>', views.start_lite),
    path('process_quiz', views.process_quiz),
    # path('quiz_heavy', views.quiz_heavy),
    path('results', views.results),
    path('logout', views.logout)
]