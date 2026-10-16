from rest_framework import serializers
from ExamApp.models import QuestionsDb

class QuestionSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=200)
    option1=serializers.CharField(max_length=200)
    option2=serializers.CharField(max_length=200)
    option3=serializers.CharField(max_length=200)
    option4=serializers.CharField(max_length=200)
    answer=serializers.CharField(max_length=200)

    
