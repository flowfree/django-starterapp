from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(minute='*/1')), ignore_result=True)
def some_task():
    print('hello, world!')