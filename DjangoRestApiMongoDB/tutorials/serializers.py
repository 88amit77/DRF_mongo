from rest_framework import serializers
from .models import Tutorial, Movie, Test1, Test2


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
                  'title',
                  'description',
                  'published')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
                  'title',
                  'description'
                  )

class Test1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test1
        fields = '__all__'


class Test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = '__all__'