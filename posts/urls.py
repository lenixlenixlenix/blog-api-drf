from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet, YourPostsView

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = [
    path("yourpost", YourPostsView.as_view()),
]



urlpatterns += router.urls

