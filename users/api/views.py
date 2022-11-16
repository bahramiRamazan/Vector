from rest_framework.decorators import  action  as detail_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import get_object_or_404


from .permissions import (
    AdminOrAuthorCanEdit,
)
from users.models import  User
from .serializers import (
    UserSerializer,
    
 
    ChangePasswordSerializer,
    PreferenceSerializer,

)

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        IsAuthenticated,
    )

    @detail_route(methods=['get'],detail="read")
    def posts(self, request, pk=None):
        queryset = Post.objects.filter(author__pk=pk).order_by('-created')

        context = {'request': request}

        serializer = PostSerializer(queryset, context=context, many=True)

        return Response(serializer.data)





##https://stackoverflow.com/questions/38845051/how-to-update-user-password-in-django-rest-framework

class ChangePasswordView(RetrieveUpdateAPIView):
    queryset= User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

#https://stackoverflow.com/questions/38845051/how-to-update-user-password-in-django-rest-framework
class ChangePreferenceApiView(APIView):
    
    serializer_class = PreferenceSerializer
    permission_classes = [AllowAny]

    def get(self, request,language):
        print("this is from get")
        user=request.user
        ser=PreferenceSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)

    


    def post(self, request, language):
        serializer_context = {"request": request}
        print(language)
        user = request.user
        print("the request data is ",request.data)
        language_prefered=language
        print("this is the language prefered",language_prefered)
        user.language_prefered=language_prefered

        user.save()

        name=user.username
        language=language_prefered

        class Preference:

            def __init__(self, language, name):
               
                self.language_prefered = language
                self.username=name
               


        pref = Preference(language,name)
        serializer = PreferenceSerializer(user)
        print(serializer.data)
        print(serializer)
      

        # serializer_context = {"request": request}
        # serializer = self.serializer_class(PreferenceSerializer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
     
