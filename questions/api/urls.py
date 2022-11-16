from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)), 

    path("questions/<slug:slug>/answers/", 
         qv.AnswerListAPIView.as_view(),
         name="answer-list"),
         
     path("questions/search/<str:keyword>/", 
     qv.SearchListAPIView.as_view(),
     name="questions-search"),


   path("category/list/", 
     qv.CategoryListAPIView.as_view(),
     name="questions-search"),


     path("category/create/", 
     qv.CategoryCreateAPIView.as_view(),
     name="questions_catergory"),  

    path("questions/<slug:slug>/answer/", 
         qv.AnswerCreateAPIView.as_view(),
         name="answer-create"),

    path("answers/<int:pk>/", 
         qv.AnswerRUDAPIView.as_view(),
         name="answer-detail"),

    path("answers/<int:pk>/like/", 
         qv.AnswerLikeAPIView.as_view(),
         name="answer-like"),


#     path("questions/", 
#          qv.SearchListAPIView.as_view(),
#          name="questions")

]