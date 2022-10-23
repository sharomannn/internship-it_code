from django.test import TestCase
from core import models
from core import factoryies



class Tag(TestCase):

    def setUp(self):
        self.tag = factoryies.Tag()

    def test_str(self):
        """Тестирование строкового представления объекта"""
        self.assertEqual(
            str(self.tag),
            self.tag.name,
            'Cтроковые представление объекта из атрибута name'
        )

    def test_str2(self):
        """Тестирование строкового представления объекта 2"""
        print('Tag', self.tag.name)
        self.assertEqual(
            str(self.tag),
            self.tag.name,
            'Cтроковые представление объекта из атрибута name'
        )


