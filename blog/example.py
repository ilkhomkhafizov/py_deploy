from rest_framework import serializers
from datetime import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='test@mail.ru', content='Content')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


serializer = CommentSerializer(comment)

json_data = JSONRenderer().render(serializer.data)

stream = io.BytesIO(json_data)
data = JSONParser().parse(stream)


serializer_request = CommentSerializer(data=data)