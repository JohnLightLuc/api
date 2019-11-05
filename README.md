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
