from rest_framework.routers import DefaultRouter
from django.urls import include, path


from users.api import views as us

router = DefaultRouter()

from .views import UserViewSet
  


router = DefaultRouter()

router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)


urlpatterns = [
 path("password/<int:pk>/change/", 
     us.ChangePasswordView.as_view(),
     name="preference"),



 path("preference/<str:language>/change/", 
     us.ChangePreferenceApiView.as_view(),
     name="preference"),
]
