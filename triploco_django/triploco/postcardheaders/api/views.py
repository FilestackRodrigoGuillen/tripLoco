from rest_framework.views import APIView

from postcardheaders.models import PostCardHeader
from rest_framework.response import Response
from postcardheaders.api.serializers import PostCardHeaderSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

'''class getPostCardHeadersView(APIView):    
    def get(self, request, *args,**kwargs):
        queryset = PostCardHeader.objects.all()
        Serializer = PostCardHeaderSerializer(queryset, many=True)
        #serializer = [i.toJSON() for i in queryset]
        return Response(Serializer.data)'''
        
class PostCardHeaderApiViewSet(ModelViewSet):
    serializer_class = PostCardHeaderSerializer
    queryset = PostCardHeader.objects.all()