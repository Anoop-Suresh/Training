from django.db import models


class TestModel(models.Model):
    name = models.CharField('Name', max_length=50, default='', blank=False)
    description = models.TextField('Description', default='')

    @property
    def testproperty(self):
        return '{} testprop'.format(self.name)
