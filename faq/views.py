from django.db import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from faq.models import Faq, Status
from faq.serializers import FaqSerializer


@api_view(["GET", "POST"])
def faq_list(request):
    """
    Show all faqs, and create a new faq.
    """
    if request.method == "GET":
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def faq(request, pk):
    """
    Get, update and delete a faq.
    """
    try:
        faq = Faq.objects.get(pk=pk)
    except Faq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FaqSerializer(faq)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FaqSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def search(request, keyword):
    if request.method == "GET":
        faq = Faq.objects.filter(
            models.Q(question__contains=keyword) | models.Q(answer__contains=keyword)
        )
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
