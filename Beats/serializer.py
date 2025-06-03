# Beats/serializer.py
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Beat

class BeatSerializer(ModelSerializer):
    artist = SerializerMethodField()
    class Meta:
        model = Beat
        fields = '__all__'

    def get_artist(self, obj):
        if not obj.artist:
            return {
                'id': obj.artist.id,
                'username': obj.artist.username
            }
        return None
