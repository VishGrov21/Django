from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('profile-feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello', views.HelloAPIView.as_view(), name='hello'),
    path('login', views.UserLoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),
]
