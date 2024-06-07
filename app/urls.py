from django.conf.global_settings import MEDIA_ROOT
from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cars/', CarsListViewSet.as_view({'get':'list'}, name='cars')),
    path('movie/', MovieListView.as_view(), name='movie'),
    path('movie/<int:id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('create/', MovieCreateView.as_view(), name='movie_create')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



