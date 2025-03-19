from django.test import TestCase

from guestroom.models import NewGuestPostCounter
from guestroom.templatetags.new_guest_post_counter_tag import count_new_guest_post


class NewGuestPostCounterTestCase(TestCase):
    def setUp(self):
        NewGuestPostCounter.objects.create(counter=0)

    def test_add_one_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        self.assertEqual(count_new_guest_post(), 1)

    def test_get_counter_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        counter.add_one()
        self.assertEqual(count_new_guest_post(), 2)

    def test_reset_counter_method(self):
        counter = NewGuestPostCounter.objects.first()
        counter.add_one()
        counter.reset_counter()
        self.assertEqual(count_new_guest_post(), 0)
