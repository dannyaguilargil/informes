from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'informes.settings')

app = Celery('informes')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.conf.timezone = 'America/Lima'


app.autodiscover_tasks()

#@app.task(bind=True)
#def debug_task(self):
#    print(f'Request: {self.request!r}')