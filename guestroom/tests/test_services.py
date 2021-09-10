from django.test import TestCase

from guestroom.models import NewGuestPostCounter


class NewGuestPostCounterTestCase(TestCase):
    def setUp(self):
        NewGuestPostCounter.objects.create(counter=0)

    def test_add_one_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        self.assertEqual(counter.get_counter(), 1)

    def test_get_counter_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        counter.add_one()
        self.assertEqual(counter.get_counter(), 2)

    def test_reset_counter_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        counter.reset_counter()
        self.assertEqual(counter.get_counter(), 0)
