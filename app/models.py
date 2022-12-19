from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
# Create your models here.





class Images(models.Model):
    image = models.ImageField(upload_to="static/db/gallery/")

    def __str__(self) -> str:
        return str(f"Image -> {self.id}")


class Gallery(models.Model):
    image = models.ImageField(upload_to="static/db/gallery/")

    def __str__(self) -> str:
        return f"Gallery -> {self.id}"



class New(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField()
    date_created = models.DateField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        
    def __str__(self):
        return self.title



class Status(models.Model):
    percent_of_graduations = models.IntegerField()
    number_of_professors = models.IntegerField()
    number_of_housing = models.IntegerField()
    number_of_students = models.IntegerField()

    def __str__(self):
        return "Universitetni umumiy ma'lumotlari"


class Workers(models.Model):
    fullname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    number = models.CharField(max_length=200, default='')
    email = models.EmailField()
    telegram = models.CharField(max_length=200, default='')
    instagram = models.CharField(max_length=200, default='')
    facebook = models.CharField(max_length=200, default='')
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")

    def __str__(self):
        return self.fullname


class Leaders(models.Model):
    fullname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    number = models.CharField(max_length=200, default='')
    email = models.EmailField()
    telegram = models.CharField(max_length=200, default='')
    instagram = models.CharField(max_length=200, default='')
    facebook = models.CharField(max_length=200, default='')
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="static/db/workers/")

    def __str__(self):
        return self.fullname


class Event(models.Model):
    in_charge = models.ForeignKey(Workers,  on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField()
    date_created = models.DateTimeField()
    image = models.ImageField(upload_to="static/db/news/")
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        
    def __str__(self):
        return self.title





class Course(models.Model):
    image = models.ImageField(upload_to="static/db/news/")
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    course_type = models.CharField(max_length=200, blank=True, null=True)
    body = HTMLField(blank=True, null=True)
    duration = models.IntegerField()
    slug = models.SlugField(blank=True, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        
    def __str__(self):
        return self.title