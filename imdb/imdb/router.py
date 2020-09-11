from movieapi.viewsets import MoviesViewset,GenreViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('movies',MoviesViewset)
router.register('genre',GenreViewset)

