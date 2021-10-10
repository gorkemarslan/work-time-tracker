from django.test import TestCase
from users.models import Employee, Role
from work_api.models import Label, Work


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.role = Role.objects.create(name='Backend Developer')
        data = {'email': 'test@test.com', 'first_name': 'Test', 'last_name': 'User'}
        self.employee = Employee.objects.create(**data)
        self.employee.role.add(self.role)
        self.label = Label.objects.create(name='Bug')


class LabelModelTests(TestCase):
    def setUp(self) -> None:
        self.label = Label.objects.create(name='Bug')

    def test_label_instance_creation(self):
        self.assertEqual(Label.objects.count(), 1)
        self.assertEqual(str(self.label), 'Bug')


class WorkModelTests(BaseTestCase):
    def setUp(self) -> None:
        super(WorkModelTests, self).setUp()
        self.work = Work.objects.create(title='Fix bug')
        self.work.employee.add(self.employee)
        self.work.label.add(self.label)

    def test_work_instance_creation(self):
        self.assertEqual(Work.objects.count(), 1)
        self.assertEqual(self.work.title, 'Fix bug')
        self.assertFalse(self.work.is_completed)
        self.assertEqual(str(self.work.label.first()), 'Bug')
        self.assertIn('ongoing', str(self.work))

    def test_work_is_completed_successfully(self):
        self.work.complete_work()
        self.assertTrue(self.work.is_completed)
        self.assertNotIn('ongoing', str(self.work))
