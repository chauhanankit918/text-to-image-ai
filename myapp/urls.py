from rest_framework.routers import SimpleRouter
from myapp.apis import TextImageViewSet


router = SimpleRouter()
router.register(r'images/text-image',
                TextImageViewSet,
                basename='text_image')

urlpatterns = router.urls
