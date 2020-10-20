from django.db.models import Model, IntegerField
from simple_diff.models import ModelDiffMixin


class TestModel(ModelDiffMixin, Model):
    number_of_things = IntegerField(default=0)
