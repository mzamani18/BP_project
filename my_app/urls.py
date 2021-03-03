from django.urls import path, include
from .views import SignUpView, check_role, student_panel, home_page
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/check/', check_role, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('',home_page,name='home_page'),
    path('action_page.php?role=student/', student_panel,name='student_panel'),
    path('professorPage/', views.professorPage, name='professorPage'),
    path('studentPage/', views.studentPage, name='studentPage'),
    path('HomeWorks/', views.HomeWorks, name='HomeWorks'),
    path('uploadVideo/', views.uploadVideo, name='uploadVideo'),
    path('uploadAnswer/', views.uploadAnswer, name='uploadAnswer'),
    path('watchVideo/', views.watchVideo, name='watchVideo'),
]
