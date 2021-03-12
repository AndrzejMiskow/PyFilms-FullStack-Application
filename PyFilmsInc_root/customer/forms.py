from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    qAdult = forms.IntegerField(label="qAdult", initial=2)
    qChild = forms.IntegerField(label="qChild", initial=2)
    qSenior = forms.IntegerField(label="qSenior", initial=2)

# seat numbers

# card details
