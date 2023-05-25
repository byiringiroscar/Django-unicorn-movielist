from django.urls import path, include
from movies.views import MovieView

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path('', MovieView.as_view())
]