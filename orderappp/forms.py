from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="name")
    quantity = forms.IntegerField(label="quantity")
    price = forms.IntegerField(label="price")