from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Post
# from .models import User
#
# User = get_user_model()
#
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#
# class UserCreateSerializer(serializers.Serializer):
#     userID = serializers.CharField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#     phone = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             userID=validated_data['userID'],
#             username=validated_data['username'],
#             phone=validated_data['phone']
#         )
#         user.set_password(validated_data['password'])
#
#         user.save()
#         return user
#
# class UserLoginSerializer(serializers.Serializer):
#     userID = serializers.CharField(max_length=10)
#     password = serializers.CharField(max_length=100, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         userID = data.get("userID", None)
#         password = data.get("password", None)
#         user = authenticate(userID=userID, password=password)
#
#         if user is None:
#             return {
#                 'userID': 'None'
#             }
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 'userID, password 없음'
#             )
#         return {
#             'userID': user.userID,
#             'token': jwt_token
#         }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text']
