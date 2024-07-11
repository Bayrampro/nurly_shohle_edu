from django.contrib import admin
from .models import *


class CourseDepAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'likes']


class LessonsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', ]


admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Hobbies)
admin.site.register(Teachers)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CourseDep, CourseDepAdmin)
admin.site.register(Videos)
admin.site.register(Service, ServiceAdmin)