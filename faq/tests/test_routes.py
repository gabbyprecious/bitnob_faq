from django.test import TestCase, Client
from django.urls import reverse
from ..models import Faq, Status

class RouteTestCase(TestCase):
    def setUp(self):
        self.faq= Faq(question="What is the world about", answer="I don't know", status=Status.ACTIVE)
        self.faq.save()

        self.faq2= Faq(question="What is Django", answer="Django is a fraemwork", status=Status.INACTIVE)
        self.faq2.save()

        self.client=Client()
    
    def test_create_faq(self):
        response = self.client.post("/faq", {"question":"What is bitnob?", "answer":"A company", "status": Status.ACTIVE})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"id", response.content)
    
    def test_fetch_faq_by_id(self):
        response = self.client.get(reverse("single_faq", args=[self.faq.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"What is the world about", response.content)
    
    def test_search_faq_with_keywords(self):
        response = self.client.post(reverse("search", kwargs={"keyword":"world about"}))
        self.assertEqual(response.status_code, 201)
        print(response.content)