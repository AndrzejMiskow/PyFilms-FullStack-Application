from django import forms
from django.contrib.auth.models import User
from API.models import Profile
from django.forms import ModelForm

class ReservationForm(forms.Form):
    # quantities of seats for reservation
    qAdult = forms.IntegerField(label="qAdult")
    qChild = forms.IntegerField(label="qChild")
    qSenior = forms.IntegerField(label="qSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")

    # card details
    cName = forms.CharField(label="cName")
    cNumber = forms.IntegerField(label="cNumber")
    cExpiration = forms.CharField(label="cExpiration")
    cCVV = forms.IntegerField(label="cCVV")


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