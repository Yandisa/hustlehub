from django import forms
from .models import Product, Message


class ProductForm(forms.ModelForm):
    """
    Form used for creating and editing a product listing.

    Allows the user to input product details such as name,
    description, price, category, and an optional image.
    """
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']


class ContactSellerForm(forms.ModelForm):
    """
    Form for users to send a message to a product seller.

    Only the message content is collected; the sender,
    receiver, and related product are set in the view.
    """
    class Meta:
        model = Message
        fields = ['message']
