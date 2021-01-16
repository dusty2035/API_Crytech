from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the user object """

    class Meta:
        model = get_user_model()
        fields = ('email', 'password','phone_number', 'first_name', 'last_name','address')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        """ Create new user with encrypted password and return it """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user



class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for the user authenticaton object """
    phone_number = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """ validate and authenicate user """
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=phone_number,
            password=password
        )

        if not user:
            msg = _('unable to authenticate with given credentials')
            raise serializers.ValidationError(msg, code='authentication')

        # when overriding validate function always must return values

        attrs["user"] = user
        return attrs