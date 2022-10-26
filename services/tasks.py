from celery import shared_task
from django.core.mail import EmailMessage,send_mail
from queryraiser.settings import DEFAULT_FROM_EMAIL as me
@shared_task(bind=True)
def approval_mail(self,query):
    email = query.user.email
    subject = 'Approval Mail - {}'.format(query.title)
    content = ''' Howdy, {}! We hope that you are doing well. This email serves as confirmation that the query {} you submitted on {} has been authorised by your respective PR and will be investigated further.
We appreciate your patience.
Best Regards
PR Team
    '''.format(query.user.username,query.title,query.date_of_creation.date())
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def rejection_mail(self,query):
    email = query.user.email
    subject = 'Rejection Mail - {}'.format(query.title)
    content = ''' Howdy, {}! We hope that you are doing well. This email serves as confirmation that your query {} submitted on {} was denied by your relevant PR due to certain charges. We will shortly contact you.
We appreciate your patience.
Best Regards
PR Team
    '''.format(query.user.username,query.title,query.date_of_creation.date())
    message = EmailMessage(subject,content,me,[email])
    message.send()
    