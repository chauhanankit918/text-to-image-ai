from django.http import JsonResponse
from myapp.tasks import generate_image


def generate_images_view():
    prompts = ["a beautiful landscape",
               "a futuristic city",
               "an abstract painting"]
    task = generate_image.delay(prompts)  # This calls the task asynchronously
    return JsonResponse({"task_id": task.id,
                         "status": "Task has been initiated."})
