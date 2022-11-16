""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
# from users.forms import SignupForm

from django.conf.urls import url
# from users import views

from django.views.generic import TemplateView



urlpatterns = [
     # url('/', views.public),
     # url(r'^api/private/', views.private),
     
     # url(r'^api/get-token/', views.get_csrf_token) ,


     url(r'^api/', include('users.api.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^', include('django.contrib.auth.urls')),

#   path('users/', include('users.urls')),
#     # path("accounts/register/",
#     #      RegistrationView.as_view(
#     #          form_class=SignupForm,
#     #          success_url="/",
#     #          ), name="django_registration_register"), 

#     path("accounts/",
#          include("django_registration.backends.one_step.urls")),

#     path("accounts/",
#          include("django.contrib.auth.urls")),


    

   

#     path("api-auth/",
#          include("rest_framework.urls")),

#     path("api/rest-auth/",
#          include("rest_auth.urls")),
        
#     path("api/rest-auth/registration/",
#          include("rest_auth.registration.urls")),


]
