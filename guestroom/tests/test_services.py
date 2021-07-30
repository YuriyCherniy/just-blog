from django.test import SimpleTestCase

from guestroom.services import NewGuestPostCounter


class NewGuestPostCounterTestCase(SimpleTestCase):
    '''
    These tests are dependent of themselves because they test a singleton class
    '''
    def setUp(self):
        self.counter = NewGuestPostCounter()

    def test_add_one_method(self):
        self.counter.add_one()
        self.assertEqual(self.counter.get_counter(), 1)

    def test_get_counter_method(self):
        self.counter.add_one()
        self.assertEqual(self.counter.get_counter(), 2)

    def test_reset_counter_method(self):
        self.counter.reset_counter()
        self.assertEqual(self.counter.get_counter(), 0)
