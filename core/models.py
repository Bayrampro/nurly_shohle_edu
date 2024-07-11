from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class CourseDep(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(verbose_name='url', )

    def get_absolute_url(self):
        return reverse('view_course', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'


class Lessons(models.Model):
    coursedep = models.ManyToManyField(CourseDep)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    slug = models.SlugField(verbose_name='url',)

    def get_absolute_url(self):
        return reverse('view_lesson', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    img1 = models.ImageField(upload_to='photos/%Y/%m/%d',)
    img2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    img3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    img4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    img5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    slug = models.SlugField(verbose_name='url',)

    def get_absolute_url(self):
        return reverse('blog_view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    lessons = models.ForeignKey(Lessons, on_delete=models.PROTECT)
    experience = models.SmallIntegerField(default=0)
    education = models.CharField(max_length=255)
    hobbies = models.ManyToManyField('Hobbies')
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.name}-{self.lessons}'


class Hobbies(models.Model):
    hobby = models.CharField(max_length=255)

    def __str__(self):
        return self.hobby


class Videos(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/%Y/%m/%d')


class Feedback(models.Model):
    user = models.CharField(max_length=255, verbose_name='Ползователь')
    email = models.EmailField(null=True)
    subject = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.email}'


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Hyzmatyň ady")
    content = models.TextField(blank=True, verbose_name="Hyzmat barada")

    def __str__(self):
        return f'{self.title}{self.content}'