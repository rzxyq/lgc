from django.test import TestCase
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from .views import fresh
from .models import NewStudent


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/freshman/')
        self.assertEqual(found.func, fresh)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = fresh(request)
        expected_html = render_to_string('freshman.html')
        self.assertEqual(response.content.decode(), expected_html)


# class ListAndItemModelsTest(TestCase):
#     def test_saving_and_retrieving_items(self):
#         list_ = List()
#         list_.save()

#         first_item = Item()
#         first_item.text = "This is the first list item"
#         first_item.list = list_
#         first_item.save()

#         second_item = Item()
#         second_item.text = "Wow this is the second item"
#         second_item.list = list_
#         second_item.save()

#         saved_list = List.objects.first()
#         self.assertEqual(saved_list, list_)

#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)

#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item.text, "This is the first list item")
#         self.assertEqual(first_saved_item.list, list_)
#         self.assertEqual(second_saved_item.text, "Wow this is the second item")
#         self.assertEqual(second_saved_item.list, list_)


# class ListViewTest(TestCase):
#     def test_display_all_items(self):
#         list_ = List.objects.create()
#         Item.objects.create(text='itemey 1', list=list_)
#         Item.objects.create(text='itemey 2', list=list_)
#         other_list = List.objects.create()
#         Item.objects.create(text='other list 1', list=other_list)
#         Item.objects.create(text='other list 2', list=other_list)

#         response = self.client.get('/lists/%d/' % (list_.id))

#         self.assertContains(response, 'itemey 1')
#         self.assertContains(response, 'itemey 2')
#         self.assertNotContains(response, 'other list 1')
#         self.assertNotContains(response, 'other list 2')

#     def test_uses_list_template(self):
#         list_ = List.objects.create()
#         response = self.client.get('/lists/%d/' % (list_.id))
#         self.assertTemplateUsed(response, 'list.html')


# class NewListTest(TestCase):
#     def test_can_save_POST_request(self):
#         other_list = List.objects.create()
#         correct_list = List.objects
#         self.client.post(
#             '/lists/new',
#             data={'item_text': 'A new list item'}
#         )

#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new list item')

#     def test_redirects_after_POST(self):
#         response = self.client.post(
#             '/lists/new',
#             data={'item_text': 'A new list item'}
#         )
#         new_list = List.objects.first()
#         self.assertRedirects(response, '/lists/%d/' % (new_list.id))

