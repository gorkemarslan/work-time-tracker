from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from work_api.models import Work
from users.emails import send_multiple_emails


@receiver(m2m_changed, sender=Work.employees.through)
def notify_users_for_role_changes(sender, instance, action, model, pk_set, **kwargs):
    if pk_set:
        employee_queryset = model.objects.filter(pk__in=pk_set)

        if action == 'post_add' or action == 'post_remove':
            # Send email when an employee is assigned or removed from a work
            send_multiple_emails([employee.email for employee in employee_queryset], action, instance)
