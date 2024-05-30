from datetime import date
from django import forms
from django.core.exceptions import ValidationError

class RentDroneForm(forms.Form):


    start_date = forms.DateField(
        required=True,
        label='Başlangıç tarihi',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                                               'focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 '
                                               'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                                               'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    start_time = forms.TimeField(
        required=True,
        label='Başlangıç saati',
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm '
                                            'rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full '
                                            'p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                                            'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    end_date = forms.DateField(
        required=True,
        label='Bitiş tarihi',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                                               'focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 '
                                               'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                                               'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    end_time = forms.TimeField(
        required=True,
        label='Bitiş saati',
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm '
                                            'rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full '
                                            'p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                                            'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('Başlangıç tarihi bitiş tarihinden büyük olamaz')
        if start_date is not None and start_date < date.today():
            raise ValidationError('Geçmiş tarihli kiralama yapamazsınız')


        if not start_date or not start_time or not end_date or not end_time:
            raise ValidationError('Boş alan bırakmayınız')

        return cleaned_data
