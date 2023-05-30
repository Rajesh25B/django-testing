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
        
        self.assertEqual(first.text, "First Item")
        self.assertEqual(second.text, "Second Item")

    def test_can_save_a_POST_request(self):
        self.client.post('', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())
