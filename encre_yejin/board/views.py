from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer
# from .serializers import UserLoginSerializer, UserCreateSerializer


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signup(request):
#     serializer = UserCreateSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return JsonResponse(serializer.data)
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signin(request):
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         response = {
#             'success': True,
#             'token': serializer.data['token']  # 시리얼라이저에서 받은 토큰 전달
#         }
#         return JsonRespoznse(response)
#
# @login_required
# def signout(request):
#     auth.logout(request)
#     del (request.session.get['user'])
#     return JsonResponse({'message':'SUCCESS'})

class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        user = User.objects.get(username=request.user)
        if serializer.is_valid():
            serializer.save(user=user)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


class PostDetail(APIView):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)

        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    @csrf_exempt
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = User.objects.get(username=request.user)
        if user == post.user:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse({'message': 'MODIFY ERROR'})
        else:
            return JsonResponse({'message': 'USER ERROR'})

    @csrf_exempt
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)

        user = User.objects.get(username=request.user)
        if user == post.user:
            post.delete()
            return JsonResponse({'message': 'DELETE SUCCESS'})
        else:
            return JsonResponse({'message' : 'USER ERROR'})
