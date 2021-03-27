from django import forms
from django.contrib.auth.models import User
from API.models import Profile
from django.forms import ModelForm
from django.core.exceptions import ValidationError
import re


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    qAdult = forms.IntegerField(label="qAdult")
    qChild = forms.IntegerField(label="qChild")
    qSenior = forms.IntegerField(label="qSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")

    # card details
    saveCard = forms.BooleanField(label="saveCard", initial=False, required=False)
    cName = forms.CharField(label="cName", required=False, initial="")
    cNumber = forms.CharField(label="cNumber", required=False, initial="")
    cExpiration = forms.CharField(label="cExpiration", required=False, initial="")
    cCVV = forms.IntegerField(label="cCVV", required=False, initial="")

    def clean_cNumber(self):
        data = self.cleaned_data['cNumber']

        # Accept 0 length as this means payment on arrival, only other length is 16
        if len(data) == 0:
            return data
        elif len(data) != 16:
            raise ValidationError('Invalid card number - not 16 digits')

        return data

    def clean_cExpiration(self):
        data = self.cleaned_data['cExpiration']

        # Accept 0 length as this means payment on arrival
        if len(data) == 0:
            return data

        # match expiry date with regex to accept only dates with format MM/YY, where MM can take
        # values between 01 - 12 (i.e. Jan - Dec), and YY between 21-29 (i.e. 2021 - 2029)
        regex = r'^(0[1-9]{1})|(1[0-2]{1})\/(2[1-9]{1})$'
        match = re.search(regex, data)
        if match is None:
            raise ValidationError('Invalid card expiry format - not MM/YY, with MM between 01-12 '
                                  'and YY between 21-29')

        return data

    def clean_cCVV(self):
        data = self.cleaned_data['cCVV']
        data_str = str(data)
        # accept only CVVs that have three of four digits, or zero if paying on arrival
        if len(data_str) == 0:
            return data
        elif len(data_str) < 3 or len(data_str) > 4:
            raise ValidationError('Invalid CVV format - not three or four digits')

        return data


class ScreeningForm(forms.Form):
    # selection of screening for given movie
    screening = forms.IntegerField(label="screening")


# forms to auto-fill edit user details page
class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('card_number', 'exp_date')
