from django.shortcuts import render
import json
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import (
    TutorialSerializer, MovieSerializer, Test1Serializer, Test2Serializer
    )
from .models import (
    Tutorial, Movie,Test1, Test2
)
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view




class TutorialViewSet(viewsets.ModelViewSet):
    search_fields = ['title','description','published','id']

    ordering_fields = ['title','description','published','id'
                       ]
    # parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class MovieViewSet(viewsets.ModelViewSet):
    search_fields = ['title','description','id']

    ordering_fields = ['title','description','id'
                       ]
    # parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class Test1ViewSet(viewsets.ModelViewSet):
    search_fields = ['id','name','age']

    ordering_fields = ['id','name','age'
                       ]
    # parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Test1.objects.all()
    serializer_class = Test1Serializer

class Test2ViewSet(viewsets.ModelViewSet):
    search_fields = ['id','title','description']

    ordering_fields = ['id','title','description'
                       ]
    # parser_classes = (MultiPartParser, FormParser)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Test2.objects.all()
    serializer_class = Test2Serializer


