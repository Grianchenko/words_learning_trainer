import random
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'word', 'translation']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many=False)
        return Response(serialized_random_word.data)


class NewWord(APIView):
    def get(self, *args, **kwargs):
        last_word = models.Words.objects.last()
        serialized_word = WordSerializer(last_word, many=False)
        return Response(serialized_word.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        new_word = models.Words.objects.create(word=data['word'],
                                               translation=data['translation'])
        new_word.save()
        serialized_new_word = WordSerializer(new_word, many=False)
        return Response(serialized_new_word.data)
