# Creat API

### Base de python

Installation

      pip install djangorestframework
      pip install markdown       # Markdown support for the browsable API.
      pip install django-filter  # Filtering support

      #Configuration

      INSTALLED_APPS = [
          ...
          'rest_framework',
      ]

### APPLICATION

->serializers.py

      from rest_framework import serializers
      from .models import *
      class Nom_model1Serializer(serializers.ModelSerializer):
          class Meta:
              model = Nom_model1
              fields = '__all__'
              depth = 1
       class Nom_model2Serializer(serializers.ModelSerializer):
          nom_model1 = Nom_model1Serializer(many=True, required=False)
          class Meta:
              model = Nom_model2
              fields = '__all__'
              depth = 1
        
->apiviews.py


        from rest_framework import viewsets
        from .models import *
        from .serializers import *
        class Nom_model1Viewset(viewsets.ModelViewSet):
            queryset = Nom_model1.objects.all()
            serializer_class = Nom_model1Serializer

        class Nom_model2Viewset(viewsets.ModelViewSet):
            queryset = Nom_model2.objects.all()
            serializer_class = Nom_model2Serializer

->views.py
 
 
        from rest_framework.routers import DefaultRouter
        from .apiviews import *

        router = DefaultRouter()
        router.register(' Nom_model1', Nom_model1Viewset, base_name=' Nom_model1')
        router.register(' Nom_model2',Nom_model2Viewset, base_name=' Nom_model2')

        urlpatterns = [
            # ...
        ]    

        urlpatterns += router.urls
        
  Api_crud : https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217
        
        
 # Autorisations, authentification et API-key
 
 ## API-key
 
 1- Installation
 
      pip installer djangorestframework-api-key
 
 2- settings.py

      INSTALLED_APPS  =  [ 
        # ... 
        "rest_framework" , 
        "rest_framework_api_key" , 
      ]
 
3 -
python manage.py migrate

4- Reglage

Gestion global de d'autorisation

      # settings.py
      REST_FRAMEWORK = {
          "DEFAULT_PERMISSION_CLASSES": [
              "rest_framework_api_key.permissions.HasAPIKey", # Autorisation HasApiKEY
              'rest_framework.permissions.IsAuthenticated',   # Autorisation par authentification
              'rest_framework.permissions.AllowAny',          # Par défaut
              'rest_framework.permissions.IsAdminUser'     # Accessible seulementt aux admins (user.is_staff= True)
              'rest_framework.permissions.IsAuthenticatedOrReadOnly' 
              'rest_framework.permissions.django.contrib.auth' # Autorisation des models
              'rest_framework.permissions.DjangoModelPermissions'
              #...
          ]
      }
      
 Fichier views
 
      from rest_framework import viewsets
      from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
      from rest_framework.response import Response
      from rest_framework_api_key.permissions import HasAPIKey
      #...
      
     class ExampleViewset(viewsets.ModelViewSet):
           permission_classes = [IsAuthenticated] 
           permission_classes = [HasAPIKey]
           permission_classes = [HasAPIKey | IsAuthenticated]
           #....
          
          
      # Autorisation en cas de non-authentification
      from rest_framework import viewsets
      from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
      from rest_framework.response import Response

       class ReadOnly(BasePermission):
          def has_permission(self, request, view):
              return request.method in SAFE_METHODS

      class ExampleViewset(viewsets.ModelViewSet):
          permission_classes = [IsAuthenticated|ReadOnly]
          #.....

         def get(self, request, format=None):
              content = {
                  'status': 'request was permitted'
              }
              return Response(content)

           
## Autorisations personnalisées

      if request.method in permissions.SAFE_METHODS:
          # Check permissions for read-only request
      else:
          # Check permissions for write request
          
        
      # autorisation vérifiant l'adresse IP et refuse la demande si l'adresse IP a été mise sur liste noire.
      
      from rest_framework import permissions

      class BlacklistPermission(permissions.BasePermission):
          """
          Global permission check for blacklisted IPs.
          """

          def has_permission(self, request, view):
              ip_addr = request.META['REMOTE_ADDR']
              blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
              return not blacklisted
              
         

## Autorisation with TokenAuthentication (https://www.youtube.com/watch?v=PFcnQbOfbUU)

1- Setting.py

    INSTALLED_APPS = [
            ...
           'rest_framework',
          'rest_framework.authtoken',
     ]

    REST_FRAMEWORK = {
          "DEFAULT_AUTHENTICATION_CLASSES":[
              'rest_framework.authentication.TokenAuthentication',
              #'rest_framework.authentication.SessionAuthentication', #Authenssion
          ],

          "DEFAULT_PERMISSION_CLASSES": [
              ....
          ]
      }
      
2-urls.py


     from rest_framework.authtoken import views
     urlpatterns = [
            ...
            path('api-token-auth/', views.obtain_auth_token, name="api-token-auth"  ),

      ]
      
      POST/ url: POST	http://127.0.0.1:8000/api-token-auth/  
            username = "...."
            password = "...."
            
      Response : 
      {
            "token": "7dde1509a1fa4b0341e3cfff3ad810d29242a979"
      }
         
         
      GET/ http://127.0.0.1:8000/api 
      
      Header:
      Authorization: Token 7dde1509a1fa4b0341e3cfff3ad810d29242a979
      
     
  ## Framework REST JWT Auth
  
      https://studygyaan.com/django/easy-rest-authorizationdjango-json-web-token
      https://jpadilla.github.io/django-rest-framework-jwt/
  
  
  
  
            

  
 Source : https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
      














