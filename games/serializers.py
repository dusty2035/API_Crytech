from rest_framework import serializers
from .models import Game


class GameSerilizer(serializers.HyperlinkedModelSerializer):
    name_img = serializers.ImageField(max_length=None , allow_empty_file=False , allow_null=True , required=False)
    main_img = serializers.ImageField(max_length=None , allow_empty_file=False , allow_null=True , required=False)
    background_img = serializers.ImageField(max_length=None , allow_empty_file=False , allow_null=True , required=False)
    class Meta :
        model = Game
        fields = ('id', 'name_img', 'alt_text', 'game_title', 'main_img', 'background_img', 'game_description', 'release_date', 'publisher_1','publisher_1_anchor', 'publisher_2', 'publisher_2_anchor', 'publisher_3', 'publisher_3_anchor', 'trailer_url', 'platform_1', 'platform_1_anchor', 'platform_2','platform_2_anchor','platform_3','platform_3_anchor',)
        