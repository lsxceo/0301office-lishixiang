#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# celeryconfig.py


from celery.schedules import crontab


CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'every-2minute-work': {
        'task': 'task.worker',
        'schedule': crontab(minute='*/2'),
    }
}
