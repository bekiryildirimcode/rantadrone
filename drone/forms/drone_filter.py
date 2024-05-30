from datetime import date

from django import forms

from drone.models import BrandModel


class DroneFilterForm(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=BrandModel.objects.all(),
        required=False,
        label='Marka',
        widget=forms.Select(attrs={'class': 'w-full  rounded border border-gray-700 '
                                            'focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900'
                                            'focus:bg-transparent text-base outline-none text-gray-900 py-1 px-3 '
                                            'leading-8 transition-colors duration-200 ease-in-out'}))

    start_date = forms.DateField(
        required=True,
        label='Başlangıç tarihi',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'w-full  rounded border border-gray-700 '
                                               'focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 '
                                               'focus:bg-transparent text-base outline-none text-gray-900 py-1 px-3 '
                                               'leading-8 transition-colors duration-200 ease-in-out'}))
    end_date = forms.DateField(
        required=False, label='Bitiş tarihi',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'w-full  rounded border border-gray-700 '
                                               'focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 '
                                               'focus:bg-transparent text-base outline-none text-gray-900 py-1 px-3 '
                                               'leading-8 transition-colors duration-200 ease-in-out'}))



    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                self.add_error("end_date", 'Başlangıç tarihi bitiş tarihinden büyük olamaz')

        if start_date is not None and start_date < date.today():
            self.add_error("end_date", 'Geçmiş tarihli kiralama yapamazsınız')

        return cleaned_data


