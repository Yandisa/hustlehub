"""
Tests for the marketplace app.

Includes test cases for the 'My Listings' view to ensure that
users only see their own product listings.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from marketplace.models import Product


class MyListingsTestCase(TestCase):
    """
    Test cases for the 'My Listings' view.

    Ensures that only listings belonging to the logged-in
    user are shown on the page.
    """

    def setUp(self):
        """
        Create two users and one product for each.
        """
        self.user = User.objects.create_user(
            username="seller",
            password="password123"
        )

        self.other_user = User.objects.create_user(
            username="buyer",
            password="password456"
        )

        # Product listed by the logged-in user
        self.product1 = Product.objects.create(
            name="Test Product 1",
            price=50,
            category="electronics",
            seller=self.user,
        )

        # Product listed by another user
        self.product2 = Product.objects.create(
            name="Test Product 2",
            price=100,
            category="fashion",
            seller=self.other_user,
        )

    def test_my_listings_view(self):
        """
        Check that the logged-in user's listings are shown
        and others are excluded.
        """
        self.client.login(
            username="seller", password="password123"
        )
        response = self.client.get(reverse("my_listings"))

        # Page should load successfully
        self.assertEqual(response.status_code, 200)

        # User should see their own product
        self.assertContains(response, "Test Product 1")

        # User should NOT see another user's product
        self.assertNotContains(response, "Test Product 2")
