from django.shortcuts import render
from .serializers import MyUserProfileSerializer
from .models import MyUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_data(request, pk):
    try:
        try:
            user = MyUser.objects.get(username=pk)
        except MyUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)
        
        serializer = MyUserProfileSerializer(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
