from rest_framework import serializers
from .models import GyanChakraUserModel


class GyanChakraUserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = GyanChakraUserModel
        fields = ['name', 'email', 'profession', 'phone', 'address', 'facebook_id_link', 'password', 'confirm_password']
    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        if confirm_password != validated_data['password']:
            raise serializers.ValidationError("Passwords do not match.")
        user = GyanChakraUserModel.objects.create_user(
            name=validated_data.get('name', ''),
            email=validated_data['email'],
            profession=validated_data.get('profession', ''),
            phone=validated_data.get('phone', ''),
            address=validated_data.get('address', ''),
            facebook_id_link=validated_data.get('facebook_id_link', ''),
            password=validated_data['password'],
        )
        return user