# Generated by Django 3.2.7 on 2021-10-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_employee_employee_id'),
        ('work_api', '0004_rename_employee_work_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='work', to='users.Employee'),
        ),
    ]
