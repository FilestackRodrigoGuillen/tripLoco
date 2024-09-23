from rest_framework.views import APIView

from users.models import User
from rest_framework.response import Response
from users.api.serializers import UserSerializer

class getUsersView(APIView):    
    def get(self, request, *args,**kwargs):
        queryset = User.objects.all()
        Serializer = UserSerializer(queryset, many=True)
        #serializer = [i.toJSON() for i in queryset]
        return Response(Serializer.data)