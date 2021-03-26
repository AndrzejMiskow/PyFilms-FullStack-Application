from django import forms


class ReservationForm(forms.Form):
    # quantities of seats for reservation
    tAdult = forms.IntegerField(label="tAdult")
    tChild = forms.IntegerField(label="tChild")
    tSenior = forms.IntegerField(label="tSenior")
    card = forms.BooleanField(required=False)

    # seat numbers
    SelectedSeatsID = forms.CharField(label="SelectedSeatsID")

    def clean(self):
        if 'card-submit' in self.data:
            self.card = True
        elif 'cash-submit' in self.data:
            self.card = False
