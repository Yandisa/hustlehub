from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Represents a product listed by a user on the marketplace.

    Fields:
        name        – Name of the product.
        description – Detailed description of the product.
        price       – Price in decimal format.
        category    – Category of the product (from predefined choices).
        seller      – User who posted the product.
        image       – Optional product image.
        created_at  – Timestamp when the product was created.
    """
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('services', 'Services'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='product_images/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Represents a message sent from one user to another
    regarding a specific product.

    Fields:
        sender     – The user who sent the message.
        receiver   – The product's seller.
        product    – The product in question.
        message    – The message content.
        timestamp  – When the message was sent.
    """
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Message from {self.sender} to {self.receiver} "
            f"about {self.product.name}"
        )
short_description = models.CharField(
    max_length=100,
    help_text="Brief summary shown in listings.",
    default="No summary provided"
)
