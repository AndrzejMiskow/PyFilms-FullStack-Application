from django import forms

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