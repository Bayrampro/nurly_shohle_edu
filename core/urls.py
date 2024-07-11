from Nurly import settings
from .views import *
from django.urls import path
urlpatterns = [
    path('', home, name='home'),
    path('course/', course, name="course"),
    path('lesson/<str:slug>/', view_lesson, name='view_lesson'),
    path('course/<str:slug>/', view_course, name='view_course'),
    path('blog/', blog, name='blog'),
    path('blog/<str:slug>/', blog_view, name='blog_view'),
    path('blog/add-like/<str:slug>/', add_like, name='add_like'),
    path('videos/', video, name='video'),
    path('signin/', user_login, name='sign-in'),
    path('signup/', create_user, name='sign-up'),
    path('logout/', user_logout, name='logout'),
    path('about/', about, name='about'),
    path('services/', services, name="services")
]
