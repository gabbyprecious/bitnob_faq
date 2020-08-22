from django.test import TestCase
from ..models import Faq, Status

class FaqModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.faq = Faq(question="What is the world about", answer="I don't know", status=Status.ACTIVE)
        cls.faq.save()
        super(FaqModelTest, cls).setUpClass()
    
    def test_a_faq_attributes_exists(self):
        self.assertEqual(self.faq.question, "What is the world about")
        self.assertEqual(self.faq.answer, "I don't know")
        self.assertEqual(self.faq.status, Status.ACTIVE)
    
    def test_deactivate_method_changes_faq_status_to_inactive(self):
        self.assertEqual(self.faq.status, Status.ACTIVE)
        self.faq.deactivate()
        self.assertEqual(self.faq.status, Status.INACTIVE)
    
    def test_deactivate_method_throws_exception_when_inactive(self):
        self.assertEqual(self.faq.status, Status.INACTIVE)
        with self.assertRaises(Exception):
            self.faq.deactivate()

    def test_faq_activate_method_changes_changes_faq_status_to_active(self):
        self.assertEqual(self.faq.status, Status.INACTIVE)
        self.faq.activate()
        self.assertEqual(self.faq.status, Status.ACTIVE)
    
    def test_faq_activate_method_throws_exception_when_active(self):
        self.assertEqual(self.faq.status, Status.ACTIVE)
        with self.assertRaises(Exception):
            self.faq.activate()

    @classmethod
    def tearDownClass(cls):
        super(FaqModelTest, cls).tearDownClass()
