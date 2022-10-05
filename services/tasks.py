from celery import shared_task
from django.core.mail import EmailMessage,send_mail
from queryraiser.settings import DEFAULT_FROM_EMAIL as me
@shared_task(bind=True)
def approval_mail(self,query):
    email = query.user.email
    subject = 'Approval Mail - {}'.format(query.title)
    content = ''' Hello {}, Hope you are doing well. This mail is for your acknowledgment that your query {} raised on {}has been approved by your respective PR and will be looked upon further.
Thank You for your patience.
Best Regards
PR Team
    '''.format(query.user.username,query.title,query.date_of_creation)
    message = EmailMessage(subject,content,me,[email])
    message.send()

@shared_task(bind=True)
def rejection_mail(self,query):
    email = query.user.email
    subject = 'Approval Mail - {}'.format(query.title)
    content = ''' Hello {}, Hope you are doing well. This mail is for your acknowledgment that your query {} raised on {} has been rejected by your respective PR for certain allegations. We will contact you soon.
Thank You for your patience.
Best Regards
PR Team
    '''.format(query.user.username,query.title,query.date_of_creation)
    message = EmailMessage(subject,content,me,[email])
    message.send()
    