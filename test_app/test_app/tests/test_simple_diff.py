from django.test import TestCase

from ..models import TestModel


class SimpleDiffTestCase(TestCase):
    def test_string_to_int(self):
        tm = TestModel.objects.create()
        tm.number_of_things = "5"

        self.assertDictEqual(tm._get_diff(), {"number_of_things": (0, 5)})
