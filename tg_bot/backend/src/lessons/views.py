from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lessons
        fields = ['pk', 'theme', 'date', 'homework', 'mark']


class LessonsTable(APIView):
    def get(self, *args, **kwargs):
        all_lessons = models.Lessons.objects.all()
        serialized_lessons_table = LessonSerializer(all_lessons, many=True)
        return Response(serialized_lessons_table.data)


class NewLesson(APIView):
    def get(self, *args, **kwargs):
        last_lesson = models.Lessons.objects.last()
        serialized_lesson = LessonSerializer(last_lesson, many=False)
        return Response(serialized_lesson.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            new_lesson = models.Lessons.objects.create(theme=data['theme'], date=data['date'],
                                                       homework=data['homework'], mark=data['mark'])
        except KeyError:
            new_lesson = models.Lessons.objects.create(theme=data['theme'], homework=data['homework'],
                                                       mark=data['mark'])

        new_lesson.save()
        serialized_new_lesson = LessonSerializer(new_lesson, many=False)
        return Response(serialized_new_lesson.data)
