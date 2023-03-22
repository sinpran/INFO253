from celery import Celery
import time
import os

broker_url = os.environ.get("CELERY_BROKER_URL"),
res_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery_app = Celery(name='worker',
                    broker=broker_url,
                    result_backend=res_backend)


@celery_app.task
def countWords(text):
    try:
        words = text.split()
        time.sleep(len(words))
        return len(words)
    except Exception as e:
        print(e)
        return str(e)