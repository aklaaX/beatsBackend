from Core.Serializers.serializers import UserSerializer
from rest_framework import serializers
from Core.models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login



# The Serializer for the Login functionnality :
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs) # This method is used to validate the data entered by the user.

        refresh = self.get_token(self.user) # get_token is a method of parent class TokenObtainPairSerializer that is used to retrieve specific token from the database based on the user detail and adding those details.
        data['user'] = UserSerializer(self.user).data # data is a dict, we are adding the field 'user' to it.
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user) # Updating the user last_login fields in the database on condition

        return data # Data is a dictionnary, it can also be a JSOn, the magic of serializer;
    


# With Django, we need to write form in order to retrieve information 
# from a post request and deal with them, With DRF we need Serializer
class RegisterSerializer(UserSerializer):

    password = serializers.CharField(max_length = 128,
        min_length = 8,
        write_only=True,
        required=True
    )
    avatar = serializers.FileField(
        required=False
    )

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'avatar',
            'password',
            'username',
            'last_name',
            'first_name',
            
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user # Do you know about array or Dict destructuring ?