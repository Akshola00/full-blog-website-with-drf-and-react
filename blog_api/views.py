from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions

class PostUserWritePermission(BasePermission):
    message = "Editiong Post is Restricted to the authour only"
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user
class Postlist(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all() 
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass