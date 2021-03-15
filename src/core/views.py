from rest_framework.viewsets import ModelViewSet
from core.serializers import CompanySerializer
from core.models import Company

class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-updated_at")