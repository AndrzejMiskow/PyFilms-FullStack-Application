from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    qAdult = forms.IntegerField(label="qAdult")
    qChild = forms.IntegerField(label="qChild")
    qSenior = forms.IntegerField(label="qSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")

    # card details
    saveCard = forms.BooleanField(label="saveCard")
    cName = forms.CharField(label="cName")
    cNumber = forms.IntegerField(label="cNumber")
    cExpiration = forms.CharField(label="cExpiration")
    cCVV = forms.IntegerField(label="cCVV")


class ScreeningForm(forms.Form):
    # selection of screening for given movie
    screening = forms.IntegerField(label="screening")