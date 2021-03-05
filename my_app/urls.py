from django.urls import path, include
from .views import SignUpView, check_role, student_panel, home_page
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/check/', check_role, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('',home_page,name='home_page'),
    path('professorPage/', views.professorPage, name='professorPage'),
    path('studentPage/', views.studentPage, name='studentPage'),
    path('uploadVideo/', views.uploadVideo, name='uploadVideo'),
    path('watchVideo/', views.watchVideo, name='watchVideo'),
    path('Upload_HomeWork/', views.Upload_HomeWork.as_view(), name='Upload_HomeWork'),
    path('my_home_works/', views.my_home_works.as_view() , name='my_home_works'),
    path('HomeWorks/', views.HomeWorks.as_view(), name='HomeWorks'),
    path('uploadAnswer/', views.uploadAnswer.as_view(), name='uploadAnswer'),
]
