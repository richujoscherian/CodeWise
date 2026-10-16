from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionsDb
from ExamApp.serializers import QuestionSerializer
# Create your views here.
class QuestionCreator(APIView):
    def get(self,request):
        qs=QuestionsDb.objects.all()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDb.objects.create(**actual_data)

            return Response(data={"message":"question added succesfully"})
        else:
            return Response(data={"error":serializer_instance.errors})




