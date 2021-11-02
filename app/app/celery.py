import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
 
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

task = app.task

@app.task(bind=True)
def debug_task(self, data):
    print(data)
