from django.shortcuts import render
from .serializers import MyUserProfileSerializer, UserRegisterSerializer, PostSerializer
from .models import MyUser,Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response


@api_view(['POST'])
def register_user(request):
    data = request.data
    serializer = UserRegisterSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_profile_data(request, pk):
    try:
        try:
            user = MyUser.objects.get(username=pk)
        except MyUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)
        
        serializer = MyUserProfileSerializer(user, many=False)

        following = False
        if request.user in user.followers.all():
            following = True
        return Response({**serializer.data, 'following': following})
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def toggleFollow(request):
    try:
        my_user = MyUser.objects.get(username=request.user.username)
        user_to_follow = MyUser.objects.get(username=request.data['username'])
    except MyUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=404)
    
    if my_user in user_to_follow.followers.all():
        user_to_follow.followers.remove(my_user)
        return Response({'message': 'User unfollowed'})
    else:
        user_to_follow.followers.add(my_user)
        return Response({'message': 'User followed'})
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def get_users_posts(request,pk):
    try:
        user = MyUser.objects.get(username=pk)
    except MyUser.DoesNotExist:
        return Response({'error':"user does not exist"})
    # reverse below relationship

    posts = user.posts.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)