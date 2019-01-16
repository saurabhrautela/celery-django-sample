from celery import shared_task
import math, time

@shared_task
def calculate_factorial(number):
    time.sleep(5)
    return math.factorial(number)