from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, data):
        self.refresh_token = RefreshToken(data["refresh"])
        return data

    def save(self, **kwargs):
        self.refresh_token.blacklist()
