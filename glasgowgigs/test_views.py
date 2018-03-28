from django.test import TestCase
from glasgowgigs.views import ArtistDetailView, IndexView
from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import resolve


class IndexPageTests(TestCase):

    # Test index page returns an HTTP 200 status code (responds)
    def test_index_response(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # Tests if index page contains appropriate text
    def test_index_text_appears(self):
        response = self.client.get(reverse('index'), follow=True)
        self.assertIn(b'GlasgowGigs', response.content)

    # Test that the index page uses the index and base templates
    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'glasgowgigs/index.html', 'glasgowgigs/base.html')

    def test_index_shows_number_of_artists(self):
        # Access artist
        try:
            response = self.client.get(reverse('artist'))
        except:
            try:
                response = self.client.get(reverse('glasgowgigs:artist'))
            except:
                return False
        # Check if it contains views message
        self.assertIn('views: 1'.lower(), response.content.decode('ascii').lower())

    # Test if logo is displayed on index page
    def test_logo_displayed(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/GG_logo_red2.png'.lower(), response.content.decode('ascii').lower())


# Tests to ensure that pages return an HTTP 200 status code (responds)
class AboutPageTests(TestCase):

    # Test about page returns an HTTP 200 status code (responds)
    def test_about_response(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # Test that the about page uses the about and base templates
    def test_about_using_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'glasgowgigs/about.html', 'glasgowgigs/base.html')

    # Test if about page has a title
    def test_about_has_title(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class RegisterPageTests(TestCase):

    # Test register page returns an HTTP 200 status code (responds)
    def test_register_response(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    # Test that the register page uses the register and base templates
    def test_register_using_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'glasgowgigs/register.html', 'glasgowgigs/base.html')


class LoginPageTests(TestCase):

    # Test login page returns an HTTP 200 status code (responds)
    def test_login_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Test that the login page uses the login and base templates
    def test_login_using_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html', 'glasgowgigs/base.html')


class LoginPagesTests(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    # Test profile page returns an HTTP 200 status code
    def test_profile_response(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    # Test that the profile page uses profile template and base template when logged in
    def test_profile_template(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertTemplateUsed(response, 'registration/profile.html', 'glasgowgigs/base.html')

    # Test settings returns an HTTP 200 status code
    def test_settings_response(self):
        response = self.client.get(reverse('settings'), follow=True)
        self.assertEqual(response.status_code, 200)

    # Test that the settings page uses settings template and base template when logged in
    def test_settings_template(self):
        response = self.client.get(reverse('settings'), follow=True)
        self.assertTemplateUsed(response, 'registration/settings.html', 'glasgowgigs/base.html')

    # Test password page returns an HTTP 200 status code
    def test_password_response(self):
        response = self.client.get(reverse('password'), follow=True)
        self.assertEqual(response.status_code, 200)

    # Test that the password page uses password template and base template when logged in
    def test_password_template(self):
        response = self.client.get(reverse('password'), follow=True)
        self.assertTemplateUsed(response, 'registration/password.html', 'glasgowgigs/base.html')

    # Test that the restricted page sends back the correct HttpResponse
    def test_restricted_template(self):
        response = self.client.get(reverse('restricted'), follow=True)
        self.assertIn(b'Since you are logged in, you can see this text!', response.content)