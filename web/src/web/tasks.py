from celery import Celery
from django.conf import settings

broker = [f'amqp://{settings.RABBITMQ_USER}:{seettings.RABBITMQ_PASSWORD}@{host}//'
          for host in settings.RABBITMQ_HOST]
app = Celery("tasks", broker=broker, broker_transport_options{'confirm_publish':True})


@app.task
def add(x, y):
    return x + y
