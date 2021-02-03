from rest_framework import viewsets, permissions
from .serializers import NewSerilizer
from .models import New
# Create your views here.


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all().order_by('-date')
    serializer_class = NewSerilizer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
