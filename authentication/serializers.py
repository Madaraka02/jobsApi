from rest_framework import serializers
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=200, min_length=6)
    username = serializers.CharField(max_length=200, min_length=6)
    # reg_no = serializers.CharField(max_length=200, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already used')})
        return super().validate(attrs) 

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)     

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    username = serializers.CharField(max_length=200, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password']


