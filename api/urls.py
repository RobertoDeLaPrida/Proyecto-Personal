from rest_framework import routers
from .views import SongViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('songs',SongViewSet,'song_api')

urlpatterns = router.urls