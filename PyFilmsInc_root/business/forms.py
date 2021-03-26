from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    tAdult = forms.IntegerField(label="tAdult")
    tChild = forms.IntegerField(label="tChild")
    tSenior = forms.IntegerField(label="tSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")
