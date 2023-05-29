from django.test import TestCase

from app1.models import Item


class TestModelItem(TestCase):
    def test_multiple_items_in_table_field(self):
        first_item = Item()
        first_item.text = "First Item"
        first_item.save()
        
        second_item = Item()
        second_item.text = "Second Item"
        second_item.save()
        
        total_items = Item.objects.all()
        self.assertEqual(len(total_items), 2)

        first = total_items[0]
        second = total_items[1]
        
        self.assertEqual(first.text, first_item.text)
        self.assertEqual(second.text, second_item.text)
