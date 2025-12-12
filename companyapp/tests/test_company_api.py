from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from userapp.factories import UserFactory



class CompanyAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory(
            email="hamed@gmail.com",
            first_name="Mohamed",
            last_name="Hamed",
            is_superuser=False,
            is_staff=False
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("company-list")  

    # -----------------------
    # ✅ Small Business Tests
    # -----------------------
    def test_create_small_business_valid(self):
        data = {
            "name": "ABC Store",
            "type": "Small Business",
            "company_details": {
                "number_of_employees": 12,
                "annual_revenue": 150000.50
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], data["name"])

    def test_create_small_business_missing_field(self):
        data = {
            "name": "ABC Store",
            "type": "Small Business",
            "company_details": {
                "number_of_employees": 12  # Missing 'annual_revenue'
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("company_details", response.data)

    # -----------------------
    # ✅ Startup Tests
    # -----------------------
    def test_create_startup_valid(self):
        data = {
            "name": "TechVision",
            "type": "Startup",
            "company_details": {
                "founders": "Ahmed, Ali",
                "funding_stage": "Seed"
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_create_startup_missing_founders(self):
        data = {
            "name": "StartupFail",
            "type": "Startup",
            "company_details": {
                "funding_stage": "Seed"
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("company_details", response.data)

    # -----------------------
    # ✅ Corporate Tests
    # -----------------------
    def test_create_corporate_valid(self):
        data = {
            "name": "BigCorp",
            "type": "Corporate",
            "company_details": {
                "departments": ["HR", "Finance"],
                "global_branches": 20
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_create_corporate_missing_branches(self):
        data = {
            "name": "BigCorpFail",
            "type": "Corporate",
            "company_details": {
                "departments": ["HR"]  # Missing 'global_branches'
            }
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("company_details", response.data)
