from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    tAdult = forms.IntegerField(label="tAdult")
    tChild = forms.IntegerField(label="tChild")
    tSenior = forms.IntegerField(label="tSenior")

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")
    
class FindResForm(forms.Form):
    # lead reservation ID
    resID = forms.CharField(label="resID")
