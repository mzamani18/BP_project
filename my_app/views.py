from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import answerform,homeworkform
from .models import Answer, HomeWork
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomeWorks(ListView):
    model= Answer
    template_name = 'my_app/HomeWorks.html'
    context_object_name = 'answers'


class uploadAnswer(CreateView):
    model =  Answer
    fields = ('title', 'studentNumber', 'author', 'pdf')
    success_url = reverse_lazy('uploadAnswer')
    template_name = 'my_app/uploadAnswer.html'


class my_home_works(ListView):
    model = HomeWork
    template_name = 'my_app/my_home_works.html'
    context_object_name = 'homeworks'


class Upload_HomeWork(CreateView):
    model = HomeWork
    fields = ('title', 'deadline','tozihat','pdf')
    success_url = reverse_lazy('Upload_HomeWork')
    template_name = 'my_app/Upload_HomeWork.html'



def home_page(raquest):
    return HttpResponse('<h1>welcome to our site</h1>'
                        '<h1>if you have account you should login</h1>'
                        '<p><a href="http://127.0.0.1:8000/login/"> http://127.0.0.1:8000/login/</a></p>'
                        '<h1>else you should signup</h1>'
                        '<p><a href="http://127.0.0.1:8000/signup/"> http://127.0.0.1:8000/signup/</a></p>')



def check_role(request):
    resp = render(request, 'check_role.html')
    return resp


def professorPage(request):
    return render(request, 'my_app/professor.html')


def studentPage(request):
    return render(request, 'my_app/student.html')


def uploadVideo(request):
    return render(request, 'my_app/uploadVideo.html')


def watchVideo(request):
    return render(request, 'my_app/watchVideo.html')


def student_panel(request):
    return HttpResponse('welcome')


