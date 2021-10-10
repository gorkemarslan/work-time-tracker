from rest_framework.viewsets import ModelViewSet
from users.serializers import EmployeeSerializer, RoleSerializer
from users.models import Employee, Role


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
