from rest_framework import serializers
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','password']


