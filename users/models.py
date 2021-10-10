from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    """
    A model class to represent `Role` schema
    """
    name = models.CharField(_('role'), max_length=127)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    A model class to represent `Employee` schema
    """
    employee_id = models.PositiveSmallIntegerField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    role = models.ManyToManyField(Role, related_name='employee')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} ({self.employee_id})'
