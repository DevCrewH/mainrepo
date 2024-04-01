from django.urls import path,include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("post", views.PostViewSet, basename="post")

post_routers = routers.NestedDefaultRouter(router, "post", lookup = "post")
post_routers.register("review", views.ReviewViewSet, basename="post-review")
post_routers.register("rating", views.RatingViewSet, basename="post-rating")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(post_routers.urls)),
]