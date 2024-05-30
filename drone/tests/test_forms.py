from django.test import TestCase
from drone.forms import RentDroneForm

class RentDroneFormTest(TestCase):
    def test_valid_form(self):
        # Start date before end date
        form = RentDroneForm(data={'start_date': '2024-05-29', 'start_time': '10:00','end_date': '2024-05-30','end_time':'10:00'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # End date before start date
        form = RentDroneForm(data={'start_date': '2024-05-30', 'start_time': '10:00','end_date': '2024-05-29','end_time':'10:00'})
        self.assertFalse(form.is_valid())
