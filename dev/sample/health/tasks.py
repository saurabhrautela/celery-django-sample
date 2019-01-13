from celery import shared_task
import time

@shared_task
def test_function():
    time.sleep( 150 )