from django import forms
from .models import *

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
