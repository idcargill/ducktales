from curses.ascii import SP
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import DuckModel, Species

class DuckTest(TestCase):

  def setUp(self):
      self.user = get_user_model().objects.create_user(
        username="tester", 
        email="tester@email.com", 
        password="fish"
      )

      self.duck = DuckModel.objects.create( 
        name = 'Drake',
        species = 'Mallard',
        is_laying = True,
        age = 5,
        owner = self.user,
        src = 'Cats',
        )

  def test_string_rep(self):
    self.assertEqual(str(self.duck.name), 'Drake')

  def test_duck_content(self):
    self.assertEqual(self.duck.name, 'Drake')
    self.assertEqual(self.duck.is_laying, True)
    self.assertEqual(self.duck.age, 5)
    self.assertEqual(self.duck.owner, self.user)

  def test_duck_list_view(self):
      response = self.client.get(reverse("duck_list"))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Drake")
      self.assertTemplateUsed(response, "duck_list.html")

  def test_duck_detail_view(self):
      response = self.client.get(reverse("duck_detail", args="1"))
      no_response = self.client.get("/100000/")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(no_response.status_code, 404)
      self.assertContains(response, "tester")
      self.assertTemplateUsed(response, "duck_detail.html")

  def test_duck_create_view(self):
      response = self.client.post(
          reverse("create_view"),
          {
              "title": "Raker",
              "description": "test",
              "purchaser": self.user.id,
          }, follow=True
      )
      self.assertContains(response, "Raker")
      self.assertRedirects(response, reverse("detail_view", args="2")) # ??? 
