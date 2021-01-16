from rest_framework import serializers
from .models import New


class NewSerilizer(serializers.HyperlinkedModelSerializer):
    img = serializers.ImageField(max_length=None , allow_empty_file=False , allow_null=True , required=False)
    class Meta :
        model = New
        fields = ('id', 'date', 'content', 'title', 'img', 'excerpt')
        