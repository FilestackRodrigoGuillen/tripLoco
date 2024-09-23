from rest_framework import serializers
from postcardheaders.models import PostCardHeader
from users.api.serializers import UserSerializer

class PostCardHeaderSerializer(serializers.ModelSerializer):
    
    user_data = UserSerializer(source="user",read_only = True)
    
    class Meta:
        model = PostCardHeader
        fields = ['id','user','user_data','photo_cover','cover_workflow','photo_flag','location_link', 'photo_weather', 'ocr_workflow',"photo_polaroid"]