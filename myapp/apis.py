from rest_framework import mixins, status, viewsets
from myapp.models import TextImage
from myapp.serializer import TextImageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from myapp.tasks import generate_image


class TextImageViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = TextImage.objects.all()
    serializer_class = TextImageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        prompt = request.data.get('prompt', None)
        if not prompt:
            return Response({"message": "Please provide prompt"})
        generate_image.delay(list(prompt))
        return Response({"message": "Successfuly Generated"},
                        status=status.HTTP_201_CREATED)
