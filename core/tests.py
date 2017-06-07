from django.test import TestCase

from core.models import Todo


class TodoModelTest(TestCase):

    def test_todo_model_should_return_string_as_define(self):
        expected = '[False] Banana - Apple'
        actual = Todo.objects.create(
            title='Banana',
            description='Apple',
            is_done=False
        ).__str__()

        self.assertEquals(actual, expected)
