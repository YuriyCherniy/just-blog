from .models import NewGuestPostCounterModel


class NewGuestPostCounter():
    def get_counter(self):
        obj = NewGuestPostCounterModel.objects.first()
        return obj

    def add_one(self):
        obj = NewGuestPostCounterModel.objects.first()
        obj.counter += 1
        obj.save()

    def reset_counter(self):
        obj = NewGuestPostCounterModel.objects.first()
        obj.counter = 0
        obj.save()
