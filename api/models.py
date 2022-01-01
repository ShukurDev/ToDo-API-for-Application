from django.db import models

# Create your models here.
class Icon(models.Model):
    icon = models.ImageField(null=True, blank=True, verbose_name='new_icon')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='icon_created')


class Image(models.Model):
    photo = models.ImageField(null=True, verbose_name='new_image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='photo_created')


class Task(models.Model):
    Date = (
        ('Today', 'Bugun'),
        ('Tomorrow', 'Ertaga'),
        ('Next_week', 'Keyingi hafta'),
    )
    title = models.CharField(max_length=300, null=True, blank=True, verbose_name='new_task')
    text = models.TextField(null=True, blank=True, verbose_name='note')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='task_created')
    date = models.CharField(choices=Date, null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True)


class List(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='title')
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, null=True)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    list = models.ManyToOneRel(Group, field_name='list', to=5)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='list_created')

    def __str__(self):
        return self.title
