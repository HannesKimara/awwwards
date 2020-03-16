from django.test import TestCase
from mimesis import Generic

from ..models import User, Profile, Project, Image, Rating


class UserModelTestCase(TestCase):
    def setUp(self):
        self.g = Generic()
        self.username = self.g.person.username()
        self.email = self.g.person.email()
        self.password = self.g.person.password()
        self.new_user = User(
            username=self.username,
            email=self.email,
            password=self.password)

    def test_isinstance(self):
        self.assertIsInstance(self.new_user, User)

    def test_save_user_method(self):
        self.new_user.save()

        self.assertIn(self.new_user, User.objects.all())

    def test_delete_user_method(self):
        self.new_user.save()
        self.new_user.delete()

        self.assertNotIn(self.new_user, User.objects.all())

    def tearDown(self):
        User.objects.all().delete()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.g = Generic()
        self.username = self.g.person.username()
        self.email = self.g.person.email()
        self.password = self.g.person.password()
        self.new_user = User(
            username=self.username,
            email=self.email,
            password=self.password)
        self.new_user.save()

        self.user_bio = self.g.text.text()
        self.user_country = self.g.address.country()
        self.user_website = self.g.internet.home_page()
        self.user_profile = Profile(
            bio=self.user_bio,
            country=self.user_country,
            website_url=self.user_website,
            user=self.new_user
        )
        self.user_profile.save_profile()

    def test_isinstance(self):
        self.assertIsInstance(self.user_profile, Profile)

    def tearDown(self):
        Profile.objects.all().delete()


class ProjectTestCase(TestCase):
    def setUp(self):
        self.g = Generic()

        self.new_user = User(
            username=self.g.person.username(),
            email=self.g.person.email(),
            password=self.g.person.password())
        self.new_user.save()

        self.project_title = self.g.text.title()
        self.description = self.g.text.text()
        self.website_url = self.g.internet.home_page()
        self.backdrop_image = self.g.person.avatar()

        self.new_project = Project(
            title=self.project_title,
            description=self.description,
            backdrop_image=self.backdrop_image,
            website_url=self.website_url,
            user=self.new_user
        )

    def test_isinstance(self):
        self.assertIsInstance(self.new_project, Project)

    def test_save_project_method(self):
        self.new_project.save_project()

        self.assertIn(self.new_project, Project.objects.all())

    def test_delete_project_method(self):
        self.new_project.save_project()
        self.new_project.delete_project()

        self.assertNotIn(self.new_project, Project.objects.all())

    def tearDown(self):
        Project.objects.all().delete()
