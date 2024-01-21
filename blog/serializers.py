from rest_framework import serializers

from .models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body')


class BlogTestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    category = serializers.CharField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    age = serializers.IntegerField()
    father_age = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.age = validated_data.get('age', instance.age)
        instance.father_age = validated_data.get('father_age',
                                                 instance.father_age)
        instance.is_active = validated_data.get('is_active',
                                                instance.is_active)
        instance.save()
        return instance

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Title-da django so'zi bo'lishi kerak!")
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Hali yoshsan (Chushpan)")
        return value

    def validate(self, data):
        if data['age'] > data['father_age']:
            raise serializers.ValidationError("Sani yoshing dadangni yoshidan kichkina")
        return data


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
