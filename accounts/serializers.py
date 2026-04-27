from rest_framework import serializers
from .models import CustomUser, Pref
from .validators import (
    validate_username,
    validate_email,
    validate_password,
    validate_tel,
    validate_pref,
)


# API serializer with same validation rules as the form layer.
class UserRegistrationSerializer(serializers.ModelSerializer):
    # Serializer for user registration API, mirroring form validation.
    password = serializers.CharField(write_only=True)
    pref = serializers.PrimaryKeyRelatedField(queryset=Pref.objects.all())

    class Meta:
        # Meta class specifying the model and fields for serialization.
        model = CustomUser
        fields = ['username', 'email', 'password', 'tel', 'pref']

    def validate_username(self, value):
        # Validates the username using the shared validator.
        return validate_username(value)

    def validate_email(self, value):
        # Validates the email using the shared validator.
        return validate_email(value)

    def validate_password(self, value):
        # Validates the password using the shared validator.
        return validate_password(value)

    def validate_tel(self, value):
        # Validates the telephone using the shared validator.
        return validate_tel(value)

    def validate_pref(self, value):
        # Validates the prefecture, ensuring it's selected.
        if not value:
            raise serializers.ValidationError('Please select a prefecture.')
        return value

    # Create user object and hash password correctly.
    def create(self, validated_data):
        # Creates and saves a new user, hashing the password.
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
