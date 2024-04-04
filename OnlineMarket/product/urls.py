from django.urls import path,include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("product", views.ProductViewSet, basename="product")

post_routers = routers.NestedDefaultRouter(router, "product", lookup = "product")
post_routers.register("review", views.ReviewViewSet, basename="product-review")
post_routers.register("rating", views.RatingViewSet, basename="product-rating")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(post_routers.urls)),
]