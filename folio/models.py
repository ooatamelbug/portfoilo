from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    job_title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    text_desc = models.TextField()
    cv = models.CharField(max_length=200, blank=True)
    resume = models.CharField(max_length=200, blank=True)
    git = models.CharField(max_length=200, blank=True)
    linked_in = models.CharField(max_length=200, blank=True)
    face = models.CharField(max_length=200, blank=True)
    tweeter = models.CharField(max_length=200, blank=True)


class AboutUser(models.Model):
    desc_one = models.TextField(blank=True)
    desc_two = models.TextField(blank=True)
    desc_three = models.TextField(blank=True)


class LanguageSkill(models.Model):
    name = models.CharField(max_length=200)
    percent = models.IntegerField()


class ServiceProvider(models.Model):
    title = models.CharField(max_length=210)
    desc = models.TextField()
    awesome = models.CharField(max_length=200)


class CustomerSaid(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    quote = models.TextField()


class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    link = models.URLField(unique=True)
    image = models.ImageField()


class SendEmail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    subject = models.CharField(max_length=200)


