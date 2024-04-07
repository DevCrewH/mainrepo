from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from . import views



urlpatterns = [
    path('savedproduct/', views.SavedProductList.as_view()),
    path('savedproduct/<int:id>', views.SavedProductDetail.as_view()),
    path('saveproduct/', views.SaveProduct.as_view()),
    

    path('savedservice/', views.SavedServiceList.as_view()),
    path('savedservice/<int:id>', views.SavedServiceDetail.as_view()),
    path('saveservice/', views.SaveService.as_view()),
    

    path('savedevent/', views.SavedEventList.as_view()),
    path('savedevent/<int:id>', views.SavedEventDetail.as_view()),
    path('saveevent/', views.SaveEvent.as_view()),

]