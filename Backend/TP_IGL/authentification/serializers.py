from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from django.utils import timezone

from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import get_user_model
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2', 'role']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        # Role validation
        role = attrs.get('role')
        if role not in dict(User.ROLE_CHOICES).keys():
            raise serializers.ValidationError("Invalid role specified")

        return attrs

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password')
        )
        user.assign_role(role)
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=155, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)
    role = serializers.CharField(max_length=20, read_only=True)
    id = serializers.IntegerField(read_only=True)  # Add id field

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'access_token', 'refresh_token' , 'role','id']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials. Please try again.")

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        tokens = user.tokens()
        id = user.id
        return {
            'email': user.email,
            'role': user.role,
            'full_name': user.get_full_name,  # Corrected usage
            "access_token": str(tokens.get('access')),
            "refresh_token": str(tokens.get('refresh')),
            'id': id,
        }