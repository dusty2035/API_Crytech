from rest_framework import viewsets, permissions
from .serializers import GameSerilizer
from .models import Game
# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('game_title')
    serializer_class = GameSerilizer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
