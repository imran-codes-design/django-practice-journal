from django import forms
class InsertForm(forms.Form):
    product_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    product_company=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'})) 
    product_price=forms.IntegerField(max_value=200,widget=forms.TextInput(attrs={'class':'form-control'}))
