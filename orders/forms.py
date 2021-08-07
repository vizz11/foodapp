from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)
    #     if not self.instance:
    #         self.fields.pop('usid')
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['usid'].disabled = True
    class Meta:
        model = Order
        fields = ['usid']
        usid = forms.CharField(widget=forms.HiddenInput())
        # exclude =['usid','is_verif','paid']

# class CustomerAddressForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomerAddressForm, self).__init__(*args, **kwargs)
#         self.fields['customer'].disabled = True
#     class Meta:
#         model = Address
#         fields = ['customer','street', 'city', 'pincode']




    