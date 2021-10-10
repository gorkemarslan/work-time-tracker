from django.test import TestCase
from users.models import Employee, Role


class RoleModelTests(TestCase):
    def setUp(self) -> None:
        self.role = Role.objects.create(name='Backend Developer')

    def test_role_instance_creation(self):
        self.assertEqual(Role.objects.count(), 1)
        self.assertEqual(str(self.role), 'Backend Developer')


class EmployeeModelsTest(TestCase):
    def setUp(self) -> None:
        self.role = Role.objects.create(name='Backend Developer')
        data = {'email': 'test@test.com', 'first_name': 'Test', 'last_name': 'User'}
        self.employee = Employee.objects.create(**data)
        self.employee.role.add(self.role)

    def test_employee_instance_creation(self):
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(self.employee.email, 'test@test.com')
        self.assertEqual(self.employee.first_name, 'Test')
        self.assertEqual(self.employee.last_name, 'User')
        self.assertEqual(str(self.employee.role.first()), 'Backend Developer')
        self.assertEqual(str(self.employee), 'Test User (1)')
