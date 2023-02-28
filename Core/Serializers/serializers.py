from rest_framework.serializers import ModelSerializer
from Core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_name',
            'first_name',
            'avatar',
            'last_login',
        ]
        
        read_only_field = ['is_active', 'id']