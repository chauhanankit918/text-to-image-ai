from django.http import JsonResponse
from myapp.tasks import generate_image


def generate_images_view():
    # prompts = ["a beautiful landscape",
    #            "a futuristic city",
    #            "an abstract painting"]
    prompts = ['A red flying dog', 'A piano ninja', 'A footballer kid']
    task = generate_image.delay(prompts)
    return JsonResponse({"task_id": task.id,
                         "status": "Task has been initiated."})
