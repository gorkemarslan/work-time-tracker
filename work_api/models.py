from django.db import models
from django.db.models.functions import Now
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from users.models import Employee


class Label(models.Model):
    """
    A model class to represent `Label` schema
    """
    name = models.CharField(_('label'), max_length=127)

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    A model class to represent `Work` schema
    """
    employees = models.ManyToManyField(Employee, related_name='work', blank=True)
    title = models.CharField(_('title'), max_length=255)
    label = models.ManyToManyField(Label, blank=True)
    start_time = models.DateTimeField(_('start_time'), auto_now_add=True)
    end_time = models.DateTimeField(_('end_time'), null=True, blank=True)
    is_completed = models.BooleanField(_('is_completed'), default=False)

    def complete_work(self):
        self.is_completed = True
        self.end_time = Now()
        self.save()

    def get_absolute_url(self):
        return f'/works/{self.id}/'

    def get_full_absolute_url(self):
        return f'{settings.SITE_DOMAIN}{self.get_absolute_url()}'

    def __str__(self):
        if self.is_completed:
            return f'{self.title} ({self.start_time} - {self.end_time})'
        return f'{self.title} ({self.start_time} - ongoing)'
