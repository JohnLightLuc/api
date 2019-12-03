# api
Base de python
Installation

      pip install djangorestframework
      pip install markdown       # Markdown support for the browsable API.
      pip install django-filter  # Filtering support

      #Configuration

      INSTALLED_APPS = [
          ...
          'rest_framework',
      ]

## APPLICATION

### serializers.py

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
        
### apiviews.py


        from rest_framework import viewsets
        from .models import *
        from .serializers import *
        class Nom_model1Viewset(viewsets.ModelViewSet):
            queryset = Nom_model1.objects.all()
            serializer_class = Nom_model1Serializer

        class Nom_model2Viewset(viewsets.ModelViewSet):
            queryset = Nom_model2.objects.all()
            serializer_class = Nom_model2Serializer

 ### views.py
 
 
        from rest_framework.routers import DefaultRouter
        from .apiviews import *

        router = DefaultRouter()
        router.register(' Nom_model1', Nom_model1Viewset, base_name=' Nom_model1')
        router.register(' Nom_model2',Nom_model2Viewset, base_name=' Nom_model2')

        urlpatterns = [
            # ...
        ]    

        urlpatterns += router.urls
        
        
 # Autorisations et API-key
 
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
           permission_classes = [HasAPIKey|IsAuthenticated|ReadOnly] 
           permission_classes = [HasAPIKey]
           #....
           
Autorisations personnalisées

      if request.method in permissions.SAFE_METHODS:
          # Check permissions for read-only request
      else:
          # Check permissions for write request
          
        
      # classe d'autorisation vérifiant l'adresse IP et refuse la demande si l'adresse IP a été mise sur liste noire.
      
      from rest_framework import permissions

      class BlacklistPermission(permissions.BasePermission):
          """
          Global permission check for blacklisted IPs.
          """

          def has_permission(self, request, view):
              ip_addr = request.META['REMOTE_ADDR']
              blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
              return not blacklisted

  
 Source : https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
      














