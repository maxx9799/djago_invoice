  
#inheriting a property  from froms module in which we having a class name "Form"

from django import forms
from .models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ( 'Seller_Name', 'Seller_Address', 'Seller_Number', 'Buyer_Address', 'Buyer_Number', 'Item', 'Quantity', 'Price')    
    
 