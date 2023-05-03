from rest_framework import serializers
from testing_api.models import User, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    usernanme = serializers.CharField(max_length=150)
    email = serializers.EmailField(allow_blank=False)


class SnippetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=False, max_length=150)
    code = serializers.CharField(style={'base_template', 'textarea.html'})
    linenos = serializers.BooleanField(default=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python3')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):

        return Snippet.objects.create(**validated_data)



    def update(self, instance, validated_data):
        
        instance.title = self.validated_data.get('title', instance.title)
        instance.code = self.validated_data.get('code', instance.code)
        instance.linenos = self.validated_data.get('linenos', instance.linenos)
        instance.language = self.validated_data.get('language', instance.language)
        instance.style = self.validated_data.get('style', instance.style)

        instance.save()
        return instance
        




