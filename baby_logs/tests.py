import datetime
import uuid
from django.test import TestCase, RequestFactory

from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Baby, Post
from .views import check_baby_owner


class BabyTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        test_user1 = User.objects.create_user(
            "testuser1", "test1@user.com", "Testuser1password"
        )
        test_user2 = User.objects.create_user(
            "testuser2", "test2@user.com", "Testuser2password"
        )

        test_user1.save()
        test_user2.save()

        self.user = test_user1

        baby_user1 = Baby.objects.create(
            first_name="useronebabyname",
            last_name="useronebabylastname",
            date_of_birth="2020-01-01",
            owner=test_user1,
            date_added=timezone.now(),
        )
        baby_user1.save()

        baby_user2 = Baby.objects.create(
            first_name="usertwobabyname",
            last_name="usertwobabylastname",
            date_of_birth="2022-01-01",
            owner=test_user2,
            date_added=timezone.now(),
        )
        baby_user2.save()

        number_of_posts = 20
        for post in range(number_of_posts):
            title = f"Post {post}"
            text = f"Text {post}"
            # date_of_event = timezone.localdate() + datetime.timedelta(days=post % 5)
            date_of_event = timezone.now()
            baby = baby_user1 if post % 2 else baby_user2

            Post.objects.create(
                baby=baby,
                title=title,
                text=text,
                date_of_event=date_of_event,
            )

    # models test
    def test_baby_model_str(self):
        baby = Baby.objects.get(id=1)
        expected_object_name = f"{baby.first_name} {baby.last_name}"
        # self.assertTrue(isinstance(baby, Baby))
        self.assertEqual(str(baby), expected_object_name)

    def test_post_model_str(self):
        post = Post.objects.get(id=1)
        # self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), post.title)

    # views test
    def test_index_page_is_accessible(self):
        response = self.client.get(reverse("baby_logs:index"))
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_login_page_if_not_logged_in(self):
        response = self.client.get(reverse("baby_logs:baby", kwargs={"baby_id": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/users/login/"))

    def test_HTTP404_for_accessing_unauthorize_baby(self):
        # trying to access test_user2 baby
        test_user2_baby = 2
        login = self.client.login(username="testuser1", password="Testuser1password")
        response = self.client.get(
            reverse("baby_logs:baby", kwargs={"baby_id": test_user2_baby})
        )
        self.assertEqual(response.status_code, 404)
