from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        self.snack = Snack.objects.create(
            name="pickle", rating=1, purchaser=self.user, description="pickle description",
            image_url="http://pickel-image-url.com", reference_url="http://pickel-reference-url.com"
        )
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "pickle")
    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.rating, 1)
    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")
    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")
    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Chicharrones",
                "description": "Low carb",
                "purchaser": self.user,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chicharrones")
        self.assertContains(response, "Low carb")
        self.assertTemplateUsed(response, "snack_create.html")
    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "rating": 3, "purchaser": self.user.id, "description": "test description", "image_url": "testimageurl.com", "reference_url": "testreferenceurl.com"}
        )
        self.assertRedirects(response, reverse("snack_detail", args="1"), target_status_code=200)
    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "rating": 3, "purchaser": self.user.id, "description": "test description", "image_url": "badurl", "reference_url": "testreferenceurl.com"
            }
        )
        self.assertEqual(response.status_code, 200)
    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
    # you can also tests models directly
    def test_model(self):
        snack = Snack.objects.create(name="tasty chips", purchaser=self.user)
        self.assertEqual(snack.name, "tasty chips")
