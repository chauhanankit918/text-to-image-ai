from time import sleep
import logging
import requests
from chaotix_ai import settings
from chaotix_ai.celery import app
from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    ReadTimeout,
    SSLError
)
from celery import shared_task
from django.core.files import File
from myapp.models import TextImage

logger = logging.getLogger(__name__)


@app.task
def my_first_task(duration=1):
    sleep(duration)
    return "first_assignment_done"


@shared_task
def generate_image(prompts):
    api_key = settings.STABILITY_KEY

    for prompt in prompts:
        image_title = prompt.replace(' ', '_')
        try:
            response = requests.post(
                "https://api.stability.ai/v2beta/stable-image/generate/ultra",
                headers={
                    "authorization": f"Bearer {api_key}",
                    "accept": "image/*"
                },
                files={"none": ''},
                data={
                    "prompt": prompt,
                    "output_format": "jpeg"}
            )
        except (ConnectTimeout, ConnectionError, ReadTimeout, SSLError) as ex:
            logger.warning(
                f"Time out or connection error: {ex}", exc_info=True)
            return "Connection error"
        else:
            if response.status_code == 200:
                open_image = image_title+(".jpeg")
                with open(open_image, 'wb') as file:
                    file.write(response.content)
                    image_file = file
                    with open(open_image, 'rb') as image_file:
                        image_file.seek(0)
                        if file:
                            instance = TextImage.objects.create(
                                title=image_title)
                            if instance:
                                instance.image.save(
                                    open_image,
                                    File(open(f"./{open_image}", "rb")))
            else:
                logger.info("Image cannot be generated")
                return f"Error occured with code: {response.status_code}"
