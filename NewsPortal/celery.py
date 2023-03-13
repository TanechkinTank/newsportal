import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekly_subscribe': {
        'task': 'News.tasks.my_job',
        'schedule': crontab(minute="*/1"), #hour=8, minute=0, day_of_week='monday'
    },
}