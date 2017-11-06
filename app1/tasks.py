from __future__ import absolute_import, unicode_literals
from celery import task
from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


@shared_task
def create_random_user_accounts(total):
    print("start")
    print(total)
    for i in range(int(total)):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)