from django.urls import path, include
from .views import SignUpView, check_role, home_page
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/check/', check_role, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('',home_page,name='home_page'),
    path('professorPage/', views.professorPage, name='professorPage'),
    path('studentPage/', views.studentPage, name='studentPage'),
    path('Upload_HomeWork/', views.Upload_HomeWork.as_view(), name='Upload_HomeWork'),
    path('my_home_works/', views.my_home_works.as_view() , name='my_home_works'),
    path('HomeWorks/', views.HomeWorks.as_view(), name='HomeWorks'),
    path('uploadAnswer/', views.uploadAnswer.as_view(), name='uploadAnswer'),
    path('uploadVideo/', views.uploadVideo.as_view(), name='uploadVideo'),
    path('watchVideo/', views.watchVideo.as_view(), name='watchVideo'),
    path('success_upload/', views.success_upload, name='success_upload' )
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
