from rest_framework import serializers
# from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import AgentAccount, MtnAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['phone_number'] = user.phone_number
        return token

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"
class MtnAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtnAccount
        fields = "__all__"


class GetUserSerializer(serializers.ModelSerializer):
    mtn_account = MtnAccountSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password','mtn_account', 'first_name', 'last_name', 'momo_agent', 'date_created', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'phone_number',
                  'mtn_account', 'momo_agent', 'first_name', 'last_name', 'date_created', )

class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('password', 'phone_number',
                  'mtn_account', 'id', 'first_name', 'last_name', "momo_agent")
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if len(attrs['password']) != 5 and type(attrs['password']) != 'int':
            raise serializers.ValidationError({"password": "Password fields error."})
        if len(attrs['phone_number']) != 9:
            raise serializers.ValidationError(
                {"phone_number": "Check Number"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            phone_number=validated_data['phone_number'],   
            mtn_account = validated_data['mtn_account'],    
            momo_agent=validated_data['momo_agent'],
            first_name=validated_data['first_name'],
            last_name = validated_data['last_name'], 

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class GetAgentAccountSerializer(serializers.ModelSerializer):
    mtn_account = MtnAccountSerializer(read_only=True)
    user = GetUserSerializer(read_only=True)
    class Meta:
        model = AgentAccount
        fields = ('agent_name', 'agent_code', 'mtn_account', 'user')


class AgentAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentAccount
        fields = ('agent_name', 'agent_code', 'mtn_account', 'user')

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
