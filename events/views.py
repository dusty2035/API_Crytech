from rest_framework import viewsets
from .serializers import EventSerilizer
from rest_framework import permissions
from .models import Event
# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerilizer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
