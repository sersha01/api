from rest_framework import serializers
from .models import User, Book

class UserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],email=validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BookSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'