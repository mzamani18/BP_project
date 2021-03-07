from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import answerform,homeworkform
from .models import Answer, HomeWork, Videos
from django.urls import reverse_lazy




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomeWorks(ListView):
    model = Answer
    template_name = 'my_app/HomeWorks.html'
    context_object_name = 'answers'


class uploadAnswer(CreateView):
    model = Answer
    fields = ('title', 'studentNumber', 'author', 'pdf')
    Answer.title= str(Answer.title)
    if Answer.title[-1]=='f':
        success_url = reverse_lazy('success_upload')
        template_name = 'my_app/uploadAnswer.html'
    else:
        success_url = reverse_lazy('unsuccess_upload')
        template_name = 'my_app/uploadAnswer.html'


class my_home_works(ListView):
    model = HomeWork
    template_name = 'my_app/my_home_works.html'
    context_object_name = 'homeworks'


class Upload_HomeWork(CreateView):
    model = HomeWork
    fields = ('title', 'deadline','tozihat','pdf')
    HomeWork.title= str(HomeWork.title)
    if HomeWork.title[-1]=='f':
        success_url = reverse_lazy('success_upload')
        template_name = 'my_app/Upload_HomeWork.html'
    else:
        success_url = reverse_lazy('unsuccess_upload')
        template_name = 'my_app/Upload_HomeWork.html'


class uploadVideo(CreateView):
    model = Videos
    fields = ('title', 'video')
    Videos.title= str(Videos.title)
    if Videos.title[-1] == '4':
        success_url = reverse_lazy('success_upload')
        template_name = 'my_app/uploadVideo.html'
    else:
        success_url = reverse_lazy('unsuccess_upload')
        template_name = 'my_app/uploadVideo.html'

class watchVideo(ListView):
    model = Videos
    template_name = 'my_app/watchVideo.html'
    context_object_name = 'videos'



def home_page(raquest):
    return HttpResponse('<h1>welcome to our site</h1>'
                        '<h1>if you have account you should login</h1>'
                        '<p><a href="http://127.0.0.1:8000/login/"> http://127.0.0.1:8000/login/</a></p>'
                        '<h1>else you should signup</h1>'
                        '<p><a href="http://127.0.0.1:8000/signup/"> http://127.0.0.1:8000/signup/</a></p>')



def check_role(request):
    return render(request, 'check_role.html')


def professorPage(request):
    return render(request, 'my_app/professor.html')


def studentPage(request):
    return render(request, 'my_app/student.html')


def success_upload(request):
    return HttpResponse('<h2>file Uploaded Successfully</h2>')


def unsuccess_upload(request):
    return HttpResponse('<h1>Error</h1>'
        '<h2> you should upload mp4/pdf file in this field</h2>')


def score_professor(request):
    return render(request,'my_app/score_professor.html')

