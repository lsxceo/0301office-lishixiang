#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# task.py


import os
import json
from datetime import datetime
from celery import Celery


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Celery('task', broker='amqp://', backend='redis://localhost')
app.config_from_object('celeryconfig')


@app.task
def worker():
    id = datetime.now().strftime('%Y-%m-%d %X')
    english = 'No matter how dark the moment, love and hope are always possible.'
    chinese = '无论眼前有多黑暗，爱和希望总有可能。'
    dic = {}
    dic['id'] = id
    dic['en'] = english
    dic['cn'] = chinese
    data_path = os.path.join(BASE_DIR, 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            data = json.load(f)
            dailysentence = data['dailysentence']
            dailysentence.append(dic)
            data['dailysentence'] = dailysentence
            with open(data_path, 'w') as f:
                json.dump(data, f)
    else:
        with open(data_path, 'w') as f:
            data = {
                'status': 0,
                'statusText': 'dailysentence',
                'dailysentence': []
            }
            data['dailysentence'].append(dic)
            json.dump(data, f)
    print(f'{id}: 完成下载！')
