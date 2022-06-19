import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from ProjectManagmentSystem.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField()
    users = models.ManyToManyField(User)
    published_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (['-published_at'])

    def __str__(self):
        return self.title


@receiver(pre_save,sender=Project)
def pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField()
    assigned_users = models.ManyToManyField(User)
    due_date = models.DateField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


@receiver(pre_save,sender=Task)
def pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


    

