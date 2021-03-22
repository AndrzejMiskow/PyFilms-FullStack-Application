from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    qAdult = forms.IntegerField(label="qAdult")
    qChild = forms.IntegerField(label="qChild")
    qSenior = forms.IntegerField(label="qSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")

    # card details
    saveCard = forms.BooleanField(label="saveCard", initial=False, required=False)
    cName = forms.CharField(label="cName", required=False)
    cNumber = forms.IntegerField(label="cNumber", required=False)
    cExpiration = forms.CharField(label="cExpiration", required=False)
    cCVV = forms.IntegerField(label="cCVV", required=False)


class ScreeningForm(forms.Form):
    # selection of screening for given movie
    screening = forms.IntegerField(label="screening")