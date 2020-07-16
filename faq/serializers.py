from rest_framework import serializers
from faq.models import Faq

# from faq.models import Faq, status_choices, A, U

A = "ACTIVE"
U = "UNACTIVE"

status_choices = [("A", ("active")), ("U", ("unactive"))]


class FaqSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(required=False, allow_blank=True, max_length=100)
    answer = serializers.CharField(required=False, allow_blank=True, max_length=100)
    status = serializers.ChoiceField(choices=status_choices, default=A)

    def create(self, validated_data):
        """
        Create a new faq.
        """
        return Faq.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing faq.
        """
        instance.question = validated_data.get("question", instance.question)
        instance.answer = validated_data.get("answer", instance.answer)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
