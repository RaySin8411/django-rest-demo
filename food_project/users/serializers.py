from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('password', 'name')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
