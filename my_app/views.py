from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.files.storage import FileSystemStorage
from .forms import answerform
from .models import Answer


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_page(raquest):
    return HttpResponse('<h1>welcome to our site</h1>'
                        '<h1>if you have account you should login</h1>'
                        'http://127.0.0.1:8000/login/'
                        '<h1>else you should signup</h1>'
                        'http://127.0.0.1:8000/signup/')


def professorPage(request):
    return render(request, 'my_app/professor.html')

def studentPage(request):
    return render(request, 'my_app/student.html')

def HomeWorks(request):
    answers=Answer.objects.all()
    return render(request, 'my_app/HomeWorks.html',{
        'answers': answers
    })

def uploadAnswer(request):
    if request.method == 'POST':
        form = answerform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadAnswer')
    else:
        form= answerform()
    return render(request, 'my_app/uploadAnswer.html', {
        'form': form
    })

def uploadVideo(request):
    return render(request, 'my_app/uploadVideo.html')

def watchVideo(request):
    return render(request, 'my_app/watchVideo.html')

def check_role(request):
    resp = render(request, 'check_role.html')
    return resp

def student_panel(request):
    return HttpResponse('welcome')



