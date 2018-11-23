from rest_framework.serializers import HyperlinkedModelSerializer

from blog.models import Post


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text',)