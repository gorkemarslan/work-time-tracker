from rest_framework.viewsets import ModelViewSet
from work_api.serializers import LabelSerializer, WorkSerializer
from work_api.models import Label, Work


class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
