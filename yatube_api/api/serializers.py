from rest_framework import serializers


from posts import models


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    pub_date = serializers.DateTimeField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=models.Group.objects.all(),
        required=False
    )
    image = serializers.ImageField(required=False)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = models.Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = models.Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = models.Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=models.User.objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = ('user', 'following')
        model = models.Follow

    def validate(self, data):
        user = self.context.get('request').user
        if data['following'] == user:
            raise serializers.ValidationError(
                'Нарциссизм тут не приветствуется'
            )
        return data
