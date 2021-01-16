from rest_framework import serializers
from .models import Event


class EventSerilizer(serializers.HyperlinkedModelSerializer):
    img = serializers.ImageField(max_length=None , allow_empty_file=False , allow_null=True , required=False)
    class Meta :
        model = Event
        fields = ('id', 'date', 'content', 'title', 'img', 'excerpt', 'place', 'headline' )
        