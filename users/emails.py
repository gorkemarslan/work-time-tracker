from django.core import mail
from django.conf import settings

EMAIL_SUBJECT_TO_BE_ASSIGNED_TO_WORK = "You are assigned to "
EMAIL_SUBJECT_TO_BE_REMOVED_FROM_WORK = "You are removed from "
EMAIL_BODY = "Click to see the work: "


def send_multiple_emails(email_address_list, action, sender):
    """
    Ref: https://docs.djangoproject.com/en/3.2/topics/email/#sending-multiple-emails
    :return:
    """
    if action == 'post_add':
        subject = EMAIL_SUBJECT_TO_BE_ASSIGNED_TO_WORK + sender.title
    elif action == 'post_remove':
        subject = EMAIL_SUBJECT_TO_BE_REMOVED_FROM_WORK + sender.title
    else:
        raise ValueError(f'{action} is not a valid action type!')

    body = EMAIL_BODY + sender.get_full_absolute_url()
    email_sender = settings.EMAIL_HOST_USER
    connection = mail.get_connection()

    # Manually open the connection
    connection.open()

    # Construct multiple messages
    email_list = []
    for email_address in email_address_list:
        email_list.append(
            mail.EmailMessage(
                subject,
                body,
                email_sender,
                [email_address]
            )
        )

    # Send multiple in a single call -
    connection.send_messages(email_list)
    # The connection was already open so send_messages() doesn't close it.
    # We need to manually close the connection.
    connection.close()
