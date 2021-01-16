from rest_framework import viewsets
from .serializers import NewSerilizer
from rest_framework import permissions
from .models import New
# Create your views here.


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all().order_by('-date')
    serializer_class = NewSerilizer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
