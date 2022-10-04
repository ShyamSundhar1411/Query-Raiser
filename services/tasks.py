from celery import shared_task
@shared_task(bind=True)
def approval_mail(self,user):
    email = user.email