from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    job_title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    text_desc = models.TextField()
    cv = models.FileField(blank=True)
    resume = models.CharField(max_length=200, blank=True)
    git = models.CharField(max_length=200, blank=True)
    linked_in = models.CharField(max_length=200, blank=True)
    face = models.CharField(max_length=200, blank=True)
    tweeter = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class AboutUser(models.Model):
    desc_one = models.TextField(blank=True)
    desc_two = models.TextField(blank=True)
    desc_three = models.TextField(blank=True)

    def __str__(self):
        return self.desc_one


class LanguageSkill(models.Model):
    name = models.CharField(max_length=200)
    percent = models.IntegerField()

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    title = models.CharField(max_length=210)
    desc = models.TextField()
    awesome = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class WorkHistory(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    pariod = models.CharField(max_length=200)
    desc = models.TextField()
    technology = models.TextField()

    def __str__(self):
        return self.name


class EducationHistory(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pariod = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class TypeWork(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='Null')

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField()
    technology = models.TextField(default='Null')
    type = models.ForeignKey(TypeWork, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class SendEmail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.email



