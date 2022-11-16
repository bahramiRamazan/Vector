from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.api.permissions import IsAuthorOrReadOnly, AllowAny
from questions.api.serializers import AnswerSerializer, QuestionSerializer, CategorySerializer
from questions.models import Answer, Question, Category



class CategoryCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class CategoryListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        return Category.objects.filter().order_by("category_name_en")

class AnswerCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)
        serializer.save(author=request_user, question=question)


class AnswerLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an answer instance to it's author."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Question."""
    print("in question viewset")
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        print("in question viewset")
        
        serializer.save(author=self.request.user)

    


class SearchListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        print("this is ok ")
        return Question.objects.filter().order_by("-created_at")
