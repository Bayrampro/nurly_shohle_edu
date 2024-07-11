from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect

from Nurly import settings
from .forms import UserLoginForm, UserRegisterForm, FeedbackForm
from .models import *


def home(request):
    lessons = Lessons.objects.all()
    random_deps = CourseDep.objects.order_by('?')[0:8]
    teachers = Teachers.objects.all()
    return render(request, 'core/index.html', {'lessons': lessons, 'random_deps': random_deps, 'teachers': teachers})


def course(request):
    lessons = Lessons.objects.all()
    paginator = Paginator(lessons, 3)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'core/courses.html', {'lessons': lessons, 'page_obj': page_obj})


def view_lesson(request, slug):
    lesson = Lessons.objects.get(slug=slug)
    course_dep = lesson.coursedep.all()
    return render(request, 'core/view_lesson.html', {"lesson": lesson, 'course_dep': course_dep})


def view_course(request, slug):
    course_dep = CourseDep.objects.get(slug=slug)
    lesson = Lessons.objects.get(coursedep__slug=slug)
    return render(request, 'core/view_course.html', {'lesson': lesson, 'course_dep': course_dep})


def blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 4)
    popular = Blog.objects.order_by()[0:4]

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'core/blog.html', {'page_obj': page_obj, 'popular': popular})


def blog_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.views = F('views') + 1
    blog.save()
    blog.refresh_from_db()
    return render(request, 'core/blog_details.html', {'blog': blog})


def add_like(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user.is_authenticated:
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)
    else:
        return redirect('sign-in')
    blog_slug = blog.slug
    url = reverse('blog_view', args=[blog_slug])

    return redirect(url)


def video(request):
    videos = Videos.objects.all()
    return render(request, 'core/videos.html', {'videos': videos})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Giriş üstünlikli amala aşyryldy!")
            return redirect('sign-in')
        else:
            messages.error(request,"Näsazlyk ýüze çykdy, täzeden synanşyň...")
    else:
        form = UserLoginForm()
    return render(request, 'core/signin.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Üstünlikli agza bolduňyz!")
            return redirect('sign-up')
        else:
            messages.error(request, "Näsazlyk ýüze çykdy, täzeden synanşyň...")
    else:
        form = UserRegisterForm()
    return render(request, 'core/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('sign-in')


def about(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            subject = form.cleaned_data['subject']
            message = f'Email: {feedback.email}\nMessage: {feedback.subject}'
            from_email = form.cleaned_data['email']  # Replace with your email address
            to_email = settings.DEFAULT_FROM_EMAIL
            mail = send_mail(subject, message, from_email, [to_email], fail_silently=True)
            if mail:
                form.save()
                messages.success(request,'Üstünlikli ugradyldy')
                return redirect('about')
            else:
                feedback.delete()
                messages.error(request, 'Internet näsazlygy ýüze çykdy')
        else:
            messages.error(request, 'Näsazlyk ýüze çykdy')
            return redirect('about')
    else:
        form = FeedbackForm()

    return render(request, 'core/about.html', {'form': form})


def services(request):
    service = Service.objects.all()
    paginator = Paginator(service, 4)
    popular = Service.objects.order_by()[0:4]

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'core/services.html', {'page_obj': page_obj, 'popular': popular})
